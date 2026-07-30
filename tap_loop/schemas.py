"""JSON Schema definitions for Loop streams."""

from hotglue_singer_sdk import typing as th

ATTRIBUTE = th.ObjectType(
    th.Property("key", th.StringType),
    th.Property("value", th.StringType),
)

DELIVERY_METHOD = th.ObjectType(
    th.Property("code", th.StringType),
    th.Property("title", th.StringType),
)

BILLING_POLICY = th.ObjectType(
    th.Property("maxCycles", th.IntegerType),
    th.Property("minCycles", th.IntegerType),
    th.Property("interval", th.StringType),
    th.Property("intervalCount", th.IntegerType),
    th.Property("anchorDay", th.IntegerType),
    th.Property("anchorMonth", th.IntegerType),
    th.Property("anchorType", th.StringType),
)

DELIVERY_POLICY = th.ObjectType(
    th.Property("interval", th.StringType),
    th.Property("intervalCount", th.IntegerType),
)

SHIPPING_ADDRESS = th.ObjectType(
    th.Property("firstName", th.StringType),
    th.Property("lastName", th.StringType),
    th.Property("phone", th.StringType),
    th.Property("company", th.StringType),
    th.Property("address1", th.StringType),
    th.Property("address2", th.StringType),
    th.Property("city", th.StringType),
    th.Property("zip", th.StringType),
    th.Property("countryCode", th.StringType),
    th.Property("provinceCode", th.StringType),
)

BILLING_ADDRESS = th.ObjectType(
    th.Property("zip", th.StringType),
    th.Property("city", th.StringType),
    th.Property("country", th.StringType),
    th.Property("address1", th.StringType),
    th.Property("province", th.StringType),
    th.Property("countryCode", th.StringType),
    th.Property("provinceCode", th.StringType),
)

CARD = th.ObjectType(
    th.Property("brand", th.StringType),
    th.Property("expiryYear", th.IntegerType),
    th.Property("expiryMonth", th.IntegerType),
    th.Property("lastDigits", th.StringType),
)

PAYMENT_METHOD = th.ObjectType(
    th.Property("id", th.IntegerType),
    th.Property("type", th.StringType),
    th.Property("card", CARD),
    th.Property("payPal", th.CustomType({"type": ["object", "string"]})),
    th.Property("status", th.StringType),
    th.Property("source", th.StringType),
)

SUBSCRIPTION_CUSTOMER = th.ObjectType(
    th.Property("id", th.IntegerType),
    th.Property("shopifyId", th.IntegerType),
    th.Property("email", th.StringType),
)

SUBSCRIPTION_LINE = th.ObjectType(
    th.Property("id", th.IntegerType),
    th.Property("productShopifyId", th.IntegerType),
    th.Property("variantShopifyId", th.IntegerType),
    th.Property("sellingPlanShopifyId", th.IntegerType),
    th.Property("sellingPlanName", th.StringType),
    th.Property("sellingPlanGroupName", th.StringType),
    th.Property("sellingPlanGroupMerchantCode", th.StringType),
    th.Property("variantTitle", th.StringType),
    th.Property("productTitle", th.StringType),
    th.Property("name", th.StringType),
    th.Property("price", th.StringType),
    th.Property("basePrice", th.NumberType),
    th.Property("discountedPrice", th.NumberType),
    th.Property("quantity", th.IntegerType),
    th.Property("sku", th.StringType),
    th.Property("isOneTimeAdded", th.BooleanType),
    th.Property("isOneTimeRemoved", th.BooleanType),
    th.Property("bundleTransactionId", th.StringType),
    th.Property("loopBundleId", th.IntegerType),
    th.Property("attributes", th.ArrayType(ATTRIBUTE)),
    th.Property("weightInGrams", th.NumberType),
    th.Property("discounts", th.CustomType({"type": ["array", "string"]})),
    th.Property("variantImage", th.StringType),
    th.Property("image", th.StringType),
)
