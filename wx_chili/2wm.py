import qrcode
from PIL import Image
import io
import os

# 定义每个表对应的页面文件名和文件夹
pages = {
    'chili_1pq': {'folder': 'pq1', 'html_file': 'first_chili.html'},
    'chili_2rs': {'folder': 'pq2', 'html_file': 'second_chili.html'},
    'chili_3st': {'folder': 'pq3', 'html_file': 'third_chili.html'},
    'chili_4uv': {'folder': 'pq4', 'html_file': 'fourth_chili.html'},
    'chili_5wx': {'folder': 'pq5', 'html_file': 'fifth_chili.html'},
    'chili_6yz': {'folder': 'pq6', 'html_file': 'sixth_chili.html'},
}

# 获取当前项目的根目录路径
project_root = os.path.abspath(os.path.dirname(__file__))

# 生成二维码
for table, page_info in pages.items():
    # 生成页面的本地文件路径
    html_path = os.path.join(project_root, page_info['folder'], page_info['html_file'])

    # 将本地文件路径转换为 file:// URL
    page_url = f'file://{html_path}'

    # 生成二维码
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(page_url)  # 将页面URL嵌入二维码
    qr.make(fit=True)

    # 将二维码保存为图像文件
    img = qr.make_image(fill='black', back_color='white')
    buffer = io.BytesIO()
    img.save(buffer, format='PNG')
    buffer.seek(0)

    # 保存二维码文件，文件名与表名对应
    with open(f'{table}_qrcode.png', 'wb') as f:
        f.write(buffer.getvalue())

    print(f'Generated QR code for {table}: {page_url}')