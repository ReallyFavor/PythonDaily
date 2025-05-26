from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from selenium import webdriver
from PIL import Image
import io
import time

class Url(BaseModel):
    url: str

class AutoPrintScreen:
    def __init__(self):
        self.count = 0
        options = webdriver.ChromeOptions()
        options.add_experimental_option('mobileEmulation', {'deviceName': 'iPhone X'})  # 模拟iPhone X浏览
        self.driver = webdriver.Chrome(options=options)

    def get_screenshot(self, url):
        self.driver.get(url)
        time.sleep(2)
        scroll_height = 0
        # 存储所有的截图
        images = []
        while True:
            # 滚动到当前高度
            self.driver.execute_script(f"window.scrollTo(0, {scroll_height})")
            time.sleep(0.5)  # 等待内容加载

            # 获取页面的总高度
            total_height = self.driver.execute_script("return document.body.scrollHeight")
            # 截图并保存到 images 列表中
            image = self.driver.get_screenshot_as_png()
            image = Image.open(io.BytesIO(image))
            scroll_height += 812
            # 如果滚动的高度已经达到了总高度，那么就退出循环
            if scroll_height >= total_height > 812:
                # 如果超出了总高度，那么就裁剪最后一张图
                diff = scroll_height - total_height
                image = image.crop((0, image.height / 2 - diff, image.width, image.height))

            images.append(image)
            print("images", image.height)
            # 更新滚动的高度

            # 如果滚动的高度已经达到了总高度，那么就退出循环
            if scroll_height >= total_height:
                break

        # 合并所有的截图
        final_image = Image.new('RGB', (images[0].width, sum(i.height for i in images)))
        current_height = 0
        for image in images:
            final_image.paste(image, (0, current_height))
            current_height += image.height

        # 保存最终的截图
        final_image.save("images/" + str(self.count) + '.png')
        self.count += 1

    def quit(self):
        self.driver.quit()

app = FastAPI()

@app.post("/screenshot/")
async def get_screenshot(url: Url):
    screenshot = AutoPrintScreen()
    try:
        screenshot.get_screenshot(url.url)
        return {"message": "Screenshot taken successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        screenshot.quit()