from aiogram.filters.callback_data import CallbackData


class MyCallbackForInline(CallbackData, prefix="my"):
    action: str
    catalog_id: int
    actual_number: int

class MyCallbackForBackAndForward(CallbackData, prefix="my"):
    action: str
    actual_number: int
    total_count: int
    catalog_id: int