import dataclasses

from requests import get


def get_catalog(url: str, cookies: dict | None = None, header: dict | None = None,) -> dict:

    request = get(url= url, cookies=cookies, headers=header)
    if request.status_code != 200:
        print(request.status_code)
        return None

    return request.json()


def get_shop_categories_info(shop_categories_info_not_sorted: dict) -> dict[str, str] | None:
    if not shop_categories_info_not_sorted:
        return None
    shop_info = {}

    shop_info["id"] = str(shop_categories_info_not_sorted.get("id"))
    shop_info["name"] = shop_categories_info_not_sorted.get("name")

    return shop_info


def get_shop_categories(shop_info_categories: dict) -> list | None:
    if not shop_info_categories:
        return None

    data_catalogs = []

    for categories in shop_info_categories.get("shop_categories"):
        shop_info = get_shop_categories_info(categories)
        data_catalogs.append(shop_info)

    return data_catalogs


def get_product_info(product_info_not_sorted: dict) -> dict[int, str, str, str, int, int] | None:
    if not product_info_not_sorted:
        return None
    product_info = {}

    product_info["id"] = product_info_not_sorted.get("id")
    product_info["name"] = product_info_not_sorted.get("name")
    product_image = product_info_not_sorted.get("images")
    if product_image is not None:
        product_info["images"] = product_image[0]
    product_info["price"] = product_info_not_sorted.get("price")
    product_info["count"] = product_info_not_sorted.get("quantity")

    return product_info


def get_catalog_info(catalog_info_not_sorted: dict) -> list | None:
    if not catalog_info_not_sorted:
        return None

    catalog_info = []

    for catalog_products in catalog_info_not_sorted.get("products"):
        if catalog_products is None:
            break

        catalog_info.append(get_product_info(catalog_products))

    return catalog_info