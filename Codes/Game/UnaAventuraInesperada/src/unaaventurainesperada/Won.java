/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package unaaventurainesperada;

import java.awt.Font;
import java.awt.Graphics2D;
import java.awt.geom.AffineTransform;

/**
 *
 * @author INGENIERIA
 */
public class Won extends ObjetoGrafico {
    private final TiempoRestante tiempoRestante;
    private final ValorPuntaje valorPuntaje;
    public Won(double x, double y, double width, double height, TiempoRestante tiempoRestante,
            ValorPuntaje valorPuntaje) {
        super(x,y,width,height,290,120);
        this.tiempoRestante=tiempoRestante;
        this.valorPuntaje=valorPuntaje;
    } 
    

    @Override
    public void paint(Graphics2D graphics2D){
        //Transladar y escalar
        AffineTransform affineTransform = graphics2D.getTransform();
        graphics2D.translate(getX(), getY());
        graphics2D.scale(getEscalaX(), getEscalaY());
        
        //Contorno Anillo
        graphics2D.setFont(new Font("sans", Font.BOLD, 30 ));
        graphics2D.drawString("You won", 0,60);   
        graphics2D.drawString("score: "+valorPuntaje.toString(), 0,80);
        graphics2D.drawString("tiempo: "+tiempoRestante.toString(), 0,100);
        //Volver a la traslacion y escalacion anterior
        graphics2D.setTransform(affineTransform);
    }
    
    
}
