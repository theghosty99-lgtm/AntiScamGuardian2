from scanner.qr_scanner import scan_qr

result = scan_qr("assets/test.png")

print("=" * 50)

if result:
    print("QR Codes Found:")

    for qr in result:
        print(qr)
else:
    print("No QR Code Found.")

print("=" * 50)