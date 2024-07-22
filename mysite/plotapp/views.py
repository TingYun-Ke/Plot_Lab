import matplotlib.pyplot as plt
import io
import urllib, base64
from django.shortcuts import render


def plot(request):
    # 建立繪圖
    plt.figure()
    plt.plot([1, 2, 3], [4, 5, 6])
    plt.title("Sample Plot")

    # 將繪圖存入緩衝區
    buffer = io.BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    # 編碼圖像
    graphic = base64.b64encode(image_png)
    graphic = graphic.decode("utf-8")

    return render(request, "plotapp/plot.html", {"graphic": graphic})
