import streamlit as st
import requests
from PIL import Image
from io import BytesIO

# --- KONFIGURASI ---
# Jika API masih di laptop, pakai ini:
URL_API = "https://ochank-remove-bg-api.hf.space/hapus-background"
# Jika nanti sudah online, ganti jadi: "https://nama-space-anda.hf.space/hapus-background"

st.set_page_config(page_title="Hapus Background Kilat", page_icon="✂️")

# --- TAMPILAN WEBSITE ---
st.title("✂️ Penghapus Background Otomatis")
st.write("Upload fotomu, dan AI akan menghapus latarnya dalam sekejap!")

# 1. Tombol Upload
file_gambar = st.file_uploader("Pilih gambar...", type=["jpg", "jpeg", "png"])

if file_gambar is not None:
    # Tampilkan gambar asli kiri-kanan
    col1, col2 = st.columns(2)
    
    with col1:
        st.header("Foto Asli")
        st.image(file_gambar, caption="Gambar yang Anda upload", use_column_width=True)

    # Tombol Proses
    if st.button("🚀 Hapus Background Sekarang"):
        with st.spinner("Sedang memproses... Tunggu sebentar ya..."):
            try:
                # 2. Kirim gambar ke API
                files = {"file": file_gambar.getvalue()}
                response = requests.post(URL_API, files=files)

                # 3. Cek hasil
                if response.status_code == 200:
                    # Ubah data response jadi gambar
                    gambar_hasil = Image.open(BytesIO(response.content))
                    
                    with col2:
                        st.header("Hasilnya ✨")
                        st.image(gambar_hasil, caption="Background hilang!", use_column_width=True)
                        
                        # Tombol Download
                        buf = BytesIO()
                        gambar_hasil.save(buf, format="PNG")
                        byte_im = buf.getvalue()
                        
                        st.download_button(
                            label="📥 Download Hasil (PNG)",
                            data=byte_im,
                            file_name="hasil_transparan.png",
                            mime="image/png"
                        )
                else:
                    st.error("Gagal memproses gambar. Pastikan API sudah nyala!")
            
            except Exception as e:
                st.error(f"Terjadi kesalahan koneksi: {e}")