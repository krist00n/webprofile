from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Route untuk halaman utama
@app.route('/')
def index():
    return render_template('index.html')

# Route API untuk mengambil data anggota
@app.route('/api/anggota', methods=['GET'])
def get_anggota():
    anggota = [
        {
            "nama": "Gilang Wahyu Pratama",
            "nim": "22.83.0904",
            "foto": "/img/gilang.jpg",
            "deskripsi": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Repellendus esse, earum tenetur illo omnis eaque laborum quas quasi sit deleniti, voluptate ratione, suscipit accusamus quod blanditiis eius non unde doloribus!"
        },
        {
            "nama": "Muhammad Hisyam Ramadhan",
            "nim": "22.83.0938",
            "foto": "/img/Hisyam.jpg",
            "deskripsi": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Ratione excepturi vitae, inventore nihil aspernatur esse molestias eligendi beatae quasi possimus est voluptatem aliquam porro repudiandae dolorum a eveniet ut quis?"
        },
        {
            "nama": "Faesal Krisna Wijaya",
            "nim": "22.83.0901",
            "foto": "/img/krisna.jpg",
            "deskripsi": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Ad, aspernatur molestiae dolores commodi doloribus accusamus perspiciatis quae illo recusandae nesciunt impedit voluptatibus labore debitis optio mollitia illum deserunt vitae accusantium."
        }
    ]
    return jsonify(anggota)

if __name__ == '__main__':
    app.run(debug=True)
