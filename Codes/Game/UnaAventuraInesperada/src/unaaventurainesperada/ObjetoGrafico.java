/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package unaaventurainesperada;

import java.awt.Graphics2D;

/**
 *
 * @author INGENIERIA
 */
public abstract class ObjetoGrafico {
    protected double x,y;
    private final double width, height;
    private final double totalWidth, totalHeight;
    private final double escalaX, escalaY;

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
