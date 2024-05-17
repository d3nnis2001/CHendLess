package com.chendless.domain;

import org.springframework.data.mongodb.core.mapping.Document;

import javax.xml.crypto.Data;
import java.awt.*;

@Document(collection="Test")
public class DataModel {
    private String name;
    private double price;
    private int sold;
    private Image img;
    public DataModel(String name, double price, int sold, Image img) {
        this.name = name;
        this.price = price;
        this.sold = sold;
        this.img = img;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public double getPrice() {
        return price;
    }

    public void setPrice(double price) {
        this.price = price;
    }

    public int getSold() {
        return sold;
    }

    public void setSold(int sold) {
        this.sold = sold;
    }

    public Image getImg() {
        return img;
    }

    public void setImg(Image img) {
        this.img = img;
    }
}
