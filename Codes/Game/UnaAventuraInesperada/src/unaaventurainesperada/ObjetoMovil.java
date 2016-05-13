/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package unaaventurainesperada;

import java.awt.Graphics2D;

/**
 *
 * @author Julian
 */
public abstract class ObjetoMovil extends ObjetoGrafico {
    public TipoDireccion direccion;
    public final double longitudPaso;

    private int op=1;

    public TipoDireccion getDireccion() {
        return direccion;
    }

    public double getLongitudPaso() {
        return longitudPaso;
    }

    public void setDireccion(TipoDireccion direccion) {
        this.direccion = direccion;
    }

    public void devolver(ObjetoGrafico objetoGrafico){
        switch(direccion){
            case derecha:
                x=objetoGrafico.x - getWidth();
                break;
            case izquierda:
                x=objetoGrafico.x + getWidth();
                break;
            case arriba:
                y=objetoGrafico.y + getHeight();
                break;
            case abajo:
                y=objetoGrafico.y - getHeight();
                break;
        }
    }
    public void alInicio(){
        x=0;
        y=0;
    }
    public void alInicio2(ObjetoGrafico objetoGrafico){
        x=0;
        y=0;
    }

    public ObjetoMovil(double x, double y, double width, double height, double totalWidth, double totalHeight,
            TipoDireccion direccion, double longitudPaso) {
        super(x, y, width, height, totalWidth, totalHeight);
        this.direccion=direccion;
        this.longitudPaso=longitudPaso;

    }

    
    public abstract void dibujarDerecha(Graphics2D graphics2D);
    public abstract void dibujarIzquierda(Graphics2D graphics2D);
    public abstract void dibujarArriba(Graphics2D graphics2D);
    public abstract void dibujarAbajo(Graphics2D graphics2D);
    public abstract void dibujarParado(Graphics2D graphics2D);
    
    
    public abstract void run();
    
    @Override
    public void paint(Graphics2D graphics2D){
        switch (direccion){
            case parado:
                dibujarParado(graphics2D);
                break;
            case derecha:
                dibujarDerecha(graphics2D);
                break;
            case izquierda:
                dibujarIzquierda(graphics2D);
                break;
            case arriba:
                dibujarArriba(graphics2D);
                break;
            case abajo:
                dibujarAbajo(graphics2D);
                break;
        }
    
    }
    
    //public void darPaso(){
    //    switch(direccion){
    //        case derecha:
    //            x+= longitudPaso;
    //            break;
    //        case izquierda:
    //            x-=longitudPaso;
    //            break;
    //        case arriba:
    //            y-=longitudPaso;
    //            break;
    //        case abajo:
    //            y+=longitudPaso;
    //            break;
    //    }
    //}
    
}

    
