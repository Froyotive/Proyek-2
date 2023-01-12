def addProduct(products, id_barang_new, nama_barang, harga_barang):
    # this function doesn't need return value
    products[id_barang_new] = {
        "id_barang": id_barang_new,
        "nama_barang": nama_barang,
        "harga_barang": harga_barang
    }
    pass  # modify this pass with your own implementation


def calculateTotalPriceAfterDiscount(totalPrice):
    # this function need return value
    # modify this return with your own implementation (consider if else threshold for the discount)
    if totalPrice >= 500000:
        potonganDiskon = 0.25*totalPrice
    elif totalPrice >= 150000:
        potonganDiskon = 0.10*totalPrice
    else:
        totalPrice == totalPrice
    totalPrice -= potonganDiskon
    return totalPrice
