def decode():
    with open("rust.msi", "wb") as wf:
        for i in range(5):
            filename = "{}.bmsi".format(i)
            with open(filename, "rb") as f:
                wf.write(f.read())
        
if __name__ == "__main__":
    decode()