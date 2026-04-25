import speedtest

st = speedtest.Speedtest()
print(f"Download Speed: {st.download() / 10**6:.2f} Mbps")
