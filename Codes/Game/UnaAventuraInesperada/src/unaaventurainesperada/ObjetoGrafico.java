/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package unaaventurainesperada;

import java.awt.Graphics2D;
import java.awt.geom.Rectangle2D;

/**
 *
 * @author INGENIERIA
 */
public abstract class ObjetoGrafico {
    protected double x,y;
    private final double width, height;
    private final double totalWidth, totalHeight;
    private final double escalaX, escalaY;
    private boolean colisionable = true;
    private boolean visible= true;

    public ObjetoGrafico(double x, double y, double width, double height, double totalWidth, double totalHeight) {
        this.x = x;
        this.y = y;
        this.width = width;
        this.height = height;
        this.totalWidth = totalWidth;
        this.totalHeight = totalHeight;
        this.escalaX = width / totalWidth;
        this.escalaY= height / totalHeight;
    }
    public boolean colisionaCon(ObjetoGrafico otro){
        if (otro == null || this == otro || ! this.isColisionable() || ! otro.isColisionable()){
            return false;
        }
        Rectangle2D rectanguloThis=new Rectangle2D.Double(this.x,this.y,this.width,this.height);
        Rectangle2D rectanguloOtro = new Rectangle2D.Double(otro.x,otro.y,otro.width,otro.height);
        return rectanguloThis.intersects(rectanguloOtro);
    }

    public boolean isVisible() {
        return visible;
    }

    public void setVisible(boolean visible) {
        this.visible = visible;
    }
    
    public boolean isColisionable() {
        return colisionable;
    }

    public void setColisionable(boolean colisionable) {
        this.colisionable = colisionable;
    }
    public double getX() {
        return x;
    }

    public double getY() {
        return y;
    }

    public double getWidth() {
        return width;
    }

    public double getHeight() {
        return height;
    }

    public double getTotalWidth() {
        return totalWidth;
    }

    public double getTotalHeight() {
        return totalHeight;
    }

    public double getEscalaX() {
        return escalaX;
    }

    public double getEscalaY() {
        return escalaY;
    }

    public void setX(double x) {
        this.x = x;
    }

    public void setY(double y) {
        this.y = y;
    }
    
    public abstract void paint(Graphics2D graphics2D);
    
    
}
