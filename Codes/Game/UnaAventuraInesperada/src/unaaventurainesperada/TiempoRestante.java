/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package unaaventurainesperada;

import java.awt.Font;
import java.awt.Graphics2D;
import java.awt.geom.AffineTransform;
import java.util.ArrayList;
import java.util.TimerTask;

/**
 *
 * @author julian
 */
public class TiempoRestante extends TimerTask{
    private final double totalWidth = 290d;
    private final double totalHeight= 100d;
    private final Lost lost;
    //Posicion, ancho y alto en el escenario
    private double x,y;
    private double width, height;
    
    //Escalas
    private double escalaX, escalaY;
    
    public short minutos=1;
    public short segundos=30;
    private short paso=1;
    private final Escenario escenario;
    public TiempoRestante(double x, double y, double width, double height, Escenario escenario,
            Lost lost) {
        this.x = x;
        this.y = y;
        this.width = width;
        this.height = height;
        this.escalaX = width / totalWidth;
        this.escalaY = height / totalHeight;
        this.escenario = escenario;
        this.lost=lost;
    } 
    
    public void decrementar() {
        if (minutos >= 0){
            segundos-=paso;
            if(segundos < 0){
                minutos--;
                segundos=59;
            }
        }
        else{
            minutos=0;
            segundos=0;

        }
        if (minutos==0 & segundos==0){
            ArrayList<ObjetoGrafico> quienes= escenario.objetosGraficos;
            for (ObjetoGrafico objetoGrafico : quienes){
                objetoGrafico.setVisible(false);
            }
            lost.setVisible(true);         
        }
    }
    
    @Override
    public String toString(){
        String cadena= "";
        cadena += (minutos >= 0 && minutos <= 9) ? "0" : "";
        cadena += minutos + ":";
        cadena += (segundos >= 0 && segundos <= 9) ? "0" : "";
        cadena+= segundos;
        return cadena;
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

    public double getEscalaX() {
        return escalaX;
    }

    public double getEscalaY() {
        return escalaY;
    }
    
    public void paint(Graphics2D graphics2D){
        //Transladar y escalar
        AffineTransform affineTransform = graphics2D.getTransform();
        graphics2D.translate(getX(), getY());
        graphics2D.scale(getEscalaX(), getEscalaY());
        
        //Contorno Anillo
        graphics2D.setFont(new Font("sans", Font.BOLD, 40 ));
        graphics2D.drawString("Tiempo: "+toString(), 0,30);
        
        
        
        
        //Volver a la traslacion y escalacion anterior
        graphics2D.setTransform(affineTransform);
    }

    @Override
    public void run() {
        decrementar();
        escenario.repaint();
    }
    
}
