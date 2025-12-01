import streamlit as st
import requests
from PIL import Image
from io import BytesIO

# ==========================================
# KONFIGURASI APLIKASI
# ==========================================

# ⚠️ PENTING: Ganti URL di bawah ini dengan link API Hugging Face Anda!
# Contoh: "https://ochank-api-hapus-bg.hf.space/hapus-background"
URL_API = "https://ochank-remove-bg-api.hf.space/hapus-background"

# Link Iklan (Direct Link Adsterra Anda)
LINK_IKLAN = "https://www.effectivegatecpm.com/uau8uvap?key=d3fcb55f18a75f0d8f8a540b508dc966"

st.set_page_config(
    page_title="Hapus Background Otomatis",
    page_icon="✂️",
    layout="centered"
)

# ==========================================
# TAMPILAN UTAMA
# ==========================================

st.title("✂️ Penghapus Background Kilat")
st.markdown("""
Aplikasi ini menggunakan **Artificial Intelligence** untuk menghapus latar belakang fotomu secara otomatis.
**Gratis & Tanpa Watermark!**
""")

st.write("---")

# 1. Upload File
file_gambar = st.file_uploader("Upload fotomu di sini (JPG/PNG)", type=["jpg", "jpeg", "png"])

if file_gambar is not None:
    # Siapkan layout 2 kolom untuk preview
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("Foto Asli")
        st.image(file_gambar, use_container_width=True)

    # Tombol Eksekusi
    # Kita taruh di tengah agar terlihat jelas
    tombol_proses = st.button("🚀 Hapus Background Sekarang", type="primary", use_container_width=True)

    if tombol_proses:
        with col2:
            with st.spinner("Sedang memproses... Tunggu sebentar..."):
                try:
                    # 2. Kirim ke API
                    files = {"file": file_gambar.getvalue()}
                    response = requests.post(URL_API, files=files)

                    # 3. Cek Hasil
                    if response.status_code == 200:
                        # Ubah bytes menjadi gambar
                        gambar_hasil = Image.open(BytesIO(response.content))
                        
                        st.success("Berhasil! ✨")
                        st.image(gambar_hasil, use_container_width=True)
                        
                        # Simpan gambar ke memori untuk tombol download
                        buf = BytesIO()
                        gambar_hasil.save(buf, format="PNG")
                        byte_im = buf.getvalue()

                        # --- BAGIAN DOWNLOAD & IKLAN ---
                        st.write("---")
                        st.caption("Pilih opsi di bawah:")
                        
                        col_dl, col_ad = st.columns(2)
                        
                        with col_dl:
                            # Tombol Download Murni
                            st.download_button(
                                label="📥 Download Gambar (PNG)",
                                data=byte_im,
                                file_name="hasil_transparan.png",
                                mime="image/png",
                                use_container_width=True
                            )
                        
                        with col_ad:
                            # Tombol Iklan (Support)
                            st.link_button(
                                label="❤️ Support Admin (Klik Iklan)",
                                url=LINK_IKLAN,
                                help="Klik untuk membantu biaya server kami",
                                use_container_width=True
                            )
                            
                    else:
                        st.error("Gagal terhubung ke server. Coba lagi nanti.")
                        st.write(f"Status Code: {response.status_code}")
                
                except Exception as e:
                    st.error(f"Terjadi kesalahan: {e}")
                    st.warning("Pastikan URL API sudah benar dan server Hugging Face sudah menyala.")

# Footer
st.write("---")

# TEKNIK SEO SEDERHANA: MENAMBAHKAN TEKS BACAAN
with st.expander("ℹ️ Cara Menggunakan & Tanya Jawab (FAQ)"):
    st.markdown("""
    ### Cara Menghapus Background Foto Online Gratis
    1. **Upload Foto:** Pilih foto JPG atau PNG dari galeri HP atau komputer Anda.
    2. **Tunggu Proses:** AI canggih kami akan memisahkan objek dari latar belakang dalam hitungan detik.
    3. **Download:** Unduh hasil foto transparan (PNG) kualitas HD.
    
    ### Kenapa Menggunakan Alat Ini?
    - **Gratis Selamanya:** Tidak perlu bayar langganan mahal.
    - **Tanpa Watermark:** Hasil bersih untuk jualan di Shopee/Tokopedia.
    - **Cepat:** Tidak perlu skill Photoshop.
    
    Alat ini cocok untuk: Reseller, UMKM, Fotografer, dan Pembuat Konten Instagram/TikTok.
    """)
st.caption("Dibuat dengan ❤️ menggunakan Python & Streamlit")