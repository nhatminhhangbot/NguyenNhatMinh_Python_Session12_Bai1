"""
- Dữ liệu đầu vào: Một danh sách cart_items chứa các dictionary, mỗi dictionary đại diện cho một sản phẩm có cấu trúc: {"id": str, "name": str, "number": int, "price": int}.
- Chức năng 1:
    + Input: Không có
    + Output: Bảng chi tiết giỏ hàng gồm STT, Mã SP, Tên Sản Phẩm, SL, Đơn Giá, Thành Tiền và 2 dòng Tổng số lượng, Tổng tiền thanh toán
- Chức năng 2:
    + Input: Mã sản phẩm (str), Tên sản phẩm (str), Số lượng (int), Đơn giá (int).
    + Output: Thêm sản phẩm mới thành công vào cart_items / Cộng dồn thành công hoặc thông báo lỗi nếu số lượng <= 0 hoặc đơn giá < 0.
- Chức năng 3:
    + Input: Mã sản phẩm (str), Số lượng mới (int).
    + Output: Cập nhật số lượng sản phẩm thành công hoặc báo lỗi (nhập số âm hoặc không tìm thấy mã).
- Chức năng 4:
    + Input: Mã sản phẩm (str).
    + Output: Xóa sản phẩm thành công khỏi danh sách hoặc báo lỗi nếu mã không tồn tại.
"""

cart_items = [
    {
        "id": "P001", 
        "name": "Dien thoai iPhone 15",
        "number": 1,
        "price": 25000000
    },
    {
        "id": "P002",
        "name": "Op lung Silicon", 
        "number": 2, 
        "price": 150000
    }
]

while True:
    print("\n--- SHOPEE CART MANAGEMENT SYSTEM ---")
    print("1. Xem chi tiết giỏ hàng & Tính tổng tiền")
    print("2. Thêm sản phẩm mới / Cộng dồn số lượng")
    print("3. Cập nhật số lượng của một sản phẩm")
    print("4. Xóa sản phẩm khỏi giỏ hàng")
    print("5. Thoát chương trình")
    choice = input("Mời bạn chọn chức năng (1-5): ").strip()

    if choice == "1":
        print("\n--- CHI TIẾT GIỎ HÀNG ---")
        print(f"{'STT':<4} | {'Mã SP':<6} | {'Tên Sản Phẩm':<25} | {'SL':<4} | {'Đơn Giá':<12} | {'Thành Tiền'}")
        print("-" * 75)

        total_quantity = 0
        total_money = 0
        ord = 1

        for item in cart_items:
            total_price = item["number"] * item["price"]

            print(f"{ord:<4} | {item["id"]:<6} | {item["name"]:<25} | {item["number"]:<4} | {item["price"]:<12} | {total_price}")

            total_quantity += item["number"]
            total_money += total_price
            ord += 1

        print(f"⇒ Tổng số lượng sản phẩm trong giỏ: {total_quantity}")
        print(f"⇒ TỔNG TIỀN THANH TOÁN: {total_money}đ")
    elif choice == "2":
        new_item_id = input("Nhập mã sản phẩm: ")

        is_exist = False
        for item in cart_items:
            if item["id"] == new_item_id:
                add_quantity = int(input("Nhập số lượng sản phẩm muốn thêm: "))
                if add_quantity <= 0:
                    print("Số lượng sản phẩm phải lớn hơn 0.")
                else:
                    item["number"] += add_quantity
                    print("Đã cộng dồn số lượng sản phẩm mới vào số lượng cũ.")
                is_exist = True
                break

        if is_exist == False:
            new_item_name = input("Nhập tên sản phẩm mới: ")
            new_item_quantity = int(input("Nhập số lượng sản phẩm mới: "))
            new_item_price = int(input("Nhập đơn giá sản phẩm mới: "))

            if new_item_quantity <= 0 or new_item_price < 0:
                print("Số lượng sản phẩm phải lớn hơn 0 hoặc đơn giá phải >= 0.")
            else:
                new_item = {
                    "id": new_item_id,
                    "name": new_item_name, 
                    "number": new_item_quantity, 
                    "price": new_item_price
                }
                cart_items.append(new_item)
                print("Thêm sản phẩm mới thành công.")
    elif choice == "3":
        item_id_to_find = input("Nhập mã sản phẩm: ")

        find = False
        for item in cart_items:
            if item["id"] == item_id_to_find:
                updated_quantity = int(input("Nhập số lượng mới: "))

                if updated_quantity <= 0:
                    print("Số lượng phải lớn hơn 0.")
                else:
                    item["number"] = updated_quantity
                    print("Cập nhật số lượng sản phẩm thành công.")
                find = True
                break

        if find == False:
            print("Mã sản phẩm không tồn tại trong giỏ hàng.")
    elif choice == "4":
        delete_id = input("Nhập mã sản phẩm muốn xóa: ")

        find = False
        for item in cart_items:
            if item["id"] == delete_id:
                cart_items.remove(item)
                print(f"Đã xóa sản phẩm {delete_id} thành công.")
                find = True
                break

        if find == False:
            print("Mã sản phẩm không tồn tại trong giỏ hàng.")
    elif choice == "5":
        print("Thoát chương trình.")
        break
    else:
        print("Lựa chọn không hợp lệ. Vui lòng nhập từ 1 đến 5.")