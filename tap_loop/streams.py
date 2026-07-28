"""Stream type classes for tap-loop."""

from __future__ import annotations

from typing import Any

from typing_extensions import override

from tap_loop.client import LoopStream
from tap_loop.schemas import (
    ATTRIBUTE,
    DELIVERY_METHOD,
    BILLING_POLICY,
    DELIVERY_POLICY,
    SHIPPING_ADDRESS,
    SUBSCRIPTION_LINE,
    SUBSCRIPTION_CUSTOMER,
    BILLING_ADDRESS,
    PAYMENT_METHOD,
)
from hotglue_singer_sdk import typing as th


class SubscriptionsStream(LoopStream):
    """Loop subscription contracts."""

    name = "subscriptions"
    path = "/subscription"
    primary_keys = ["id"]
    replication_key = "updatedAt"
    schema = th.PropertiesList(
        th.Property("id", th.IntegerType),
        th.Property("shopifyId", th.IntegerType),
        th.Property("originOrderShopifyId", th.IntegerType),
        th.Property("createdAt", th.DateTimeType),
        th.Property("updatedAt", th.DateTimeType),
        th.Property("orderNote", th.StringType),
        th.Property("totalLineItemPrice", th.NumberType),
        th.Property("totalLineItemDiscountedPrice", th.NumberType),
        th.Property("deliveryPrice", th.NumberType),
        th.Property("currencyCode", th.StringType),
        th.Property("status", th.StringType),
        th.Property("cancellationReason", th.StringType),
        th.Property("cancellationComment", th.StringType),
        th.Property("completedOrdersCount", th.IntegerType),
        th.Property("pausedAt", th.DateTimeType),
        th.Property("cancelledAt", th.DateTimeType),
        th.Property("attributes", th.ArrayType(ATTRIBUTE)),
        th.Property("isPrepaid", th.BooleanType),
        th.Property("isMarkedForCancellation", th.BooleanType),
        th.Property("nextBillingDateEpoch", th.IntegerType),
        th.Property("lastPaymentStatus", th.StringType),
        th.Property("lastInventoryAction", th.StringType),
        th.Property("deliveryMethod", DELIVERY_METHOD),
        th.Property("billingPolicy", BILLING_POLICY),
        th.Property("deliveryPolicy", DELIVERY_POLICY),
        th.Property("shippingAddress", SHIPPING_ADDRESS),
        th.Property("lines", th.ArrayType(SUBSCRIPTION_LINE)),
        th.Property("customer", SUBSCRIPTION_CUSTOMER),
        th.Property("discounts", th.CustomType({"type": ["array", "string"]})),
        th.Property("prepaidCredits", th.CustomType({"type": ["object", "string"]})),
        th.Property("customerPaymentMethodId", th.IntegerType),
        th.Property("billingAddress", BILLING_ADDRESS),
        th.Property("isMigrated", th.BooleanType),
        th.Property("paymentMethod", PAYMENT_METHOD),
    ).to_dict()


class CustomersStream(LoopStream):
    """Loop customers with subscription counts."""

    name = "customers"
    path = "/customer"
    primary_keys = ["id"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property("id", th.IntegerType),
        th.Property("firstName", th.StringType),
        th.Property("lastName", th.StringType),
        th.Property("email", th.StringType),
        th.Property("shopifyId", th.IntegerType),
        th.Property("phone", th.StringType),
        th.Property("activeSubscriptionsCount", th.IntegerType),
        th.Property("pausedSubscriptionsCount", th.IntegerType),
        th.Property("cancelledSubscriptionsCount", th.IntegerType),
        th.Property("expiredSubscriptionsCount", th.IntegerType),
        th.Property("allSubscriptionsCount", th.IntegerType),
    ).to_dict()


class ProductsStream(LoopStream):
    """Loop products and selling-plan mapping status."""

    name = "products"
    path = "/product"
    primary_keys = ["shopifyId"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property("shopifyId", th.IntegerType),
        th.Property("title", th.StringType),
        th.Property(
            "productVariants",
            th.ArrayType(
                th.ObjectType(
                    th.Property("title", th.StringType),
                    th.Property("shopifyId", th.IntegerType),
                    th.Property("image", th.StringType),
                    th.Property("sku", th.StringType),
                    th.Property("price", th.StringType),
                    th.Property("hasSellingPlan", th.BooleanType),
                )
            ),
        ),
    ).to_dict()

    @override
    def get_url_params(
        self,
        context: dict | None,
        next_page_token: Any | None,
    ) -> dict[str, Any]:
        params = super().get_url_params(context, next_page_token)
        params["type"] = "ALL"
        return params
