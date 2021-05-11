msipath = "D:\\Users\\y\\Downloads\\rust-1.52.0-x86_64-pc-windows-gnu.msi"

def encode():
    with open(msipath, "rb") as f:
        times = 0
        while True:
            if times >= 4:
                break
            with open("./{}.bmsi".format(times), "wb") as wf:
                for i in range(100):
                    bytes = f.read(500*1024)
                    wf.write(bytes)
            times += 1
        with open("./4.bmsi", "wb") as wf:
            wf.write(f.read())


if __name__ == "__main__":
    encode()
