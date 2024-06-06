from requests import get
from .templates import PRODUCT


def get_catalog(url: str, cookies: dict | None = None, header: dict | None = None) -> dict | None:

    header = {"Authorization": header}

    response = get(url=url, cookies=cookies, headers = header)
    if response.status_code != 200:
        print(response.status_code)
        return None

    return response.json()



def get_shop_categories_info(shop_categories_info_not_sorted: dict) -> dict | None:
    if not shop_categories_info_not_sorted:
        return None

    shop_info = {}

    shop_info["id"] = str(shop_categories_info_not_sorted.get("id"))
    shop_info["name"] = shop_categories_info_not_sorted.get("name")

    return shop_info


def get_shop_categories(shop_info_categories: dict) -> list[dict] | None:
    if not shop_info_categories:
        return None

    data_catalogs = []

    for categories in shop_info_categories.get("shop_categories"):
        shop_info = get_shop_categories_info(categories)
        data_catalogs.append(shop_info)

    return data_catalogs


def get_product_info(product_info_not_sorted: dict) -> dict | None:
    if not product_info_not_sorted:
        return None
    product_info = {}

    product_info["id"] = str(product_info_not_sorted.get("id"))
    product_info["name"] = product_info_not_sorted.get("name")
    product_image = product_info_not_sorted.get("images")
    if product_image is not None:
        product_info["images"] = product_image[0]
    product_info["price"] = str(product_info_not_sorted.get("price"))
    product_info["count"] = str(product_info_not_sorted.get("quantity"))

    return product_info


def get_catalog_info(catalog_info_not_sorted: dict) -> list[dict] | None:
    if not catalog_info_not_sorted:
        return None

    catalog_info = []

    for catalog_products in catalog_info_not_sorted.get("products"):
        if catalog_products is None:
            break
        catalog_info.append(get_product_info(catalog_products))

    return catalog_info


def print_catalog(catalog: list[dict]) -> tuple[list[str], list[str]]:
    photos = []
    formated_posts = []
    for product in catalog:
        formated_posts.append(PRODUCT.format(product.get("name"), product.get("price"), product.get("count")))
        photos.append(product.get("images"))
    return (formated_posts, photos)