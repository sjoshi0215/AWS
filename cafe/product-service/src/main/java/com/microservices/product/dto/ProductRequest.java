package com.microservices.product.dto;

import java.math.BigDecimal;

public class ProductRequest {

    private String name;
    private String description;
    private BigDecimal price;
    private String currency;
    private Integer quantityAvailable;

    public ProductRequest() {}

    public ProductRequest(String name, String description, BigDecimal price, String currency, Integer quantityAvailable) {
        this.name = name;
        this.description = description;
        this.price = price;
        this.currency = currency;
        this.quantityAvailable = quantityAvailable;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public BigDecimal getPrice() {
        return price;
    }

    public void setPrice(BigDecimal price) {
        this.price = price;
    }

    public String getCurrency() {
        return currency;
    }

    public void setCurrency(String currency) {
        this.currency = currency;
    }

    public Integer getQuantityAvailable() {
        return quantityAvailable;
    }

    public void setQuantityAvailable(Integer quantityAvailable) {
        this.quantityAvailable = quantityAvailable;
    }
}
