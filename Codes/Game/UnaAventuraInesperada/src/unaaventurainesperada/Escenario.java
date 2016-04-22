/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

package unaaventurainesperada;

import java.awt.Canvas;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Image;
import java.awt.geom.AffineTransform;
import java.util.ArrayList;
import java.util.Timer;
import javax.swing.JFrame;


/**
 *
 * @author usuario
 */
public class Escenario extends Canvas {
    private int x;
    private int y;
    private JFrame marco;
    private final double totalWidth=280.0d;
    private final double totalHeight=220.0d;
    private int width, height;
    private double escalaX, escalaY;
    private final ArrayList<ObjetoGrafico> objetosGraficos;
    private final Ricardo ricardo;
    private final LlaveRoja r_contador;
    private final LlaveVerde v_contador;
    private final LlaveAzul b_contador;
    private final LlaveAmarilla a_contador;
    private final TiempoRestante tiempoRestante;
    private final Eva eva;
    



    public ArrayList<ObjetoGrafico> conQuienesColisiona(ObjetoGrafico objetoGrafico){
        ArrayList<ObjetoGrafico> quienes = new ArrayList<>();
        for (ObjetoGrafico o: objetosGraficos){
            if(objetoGrafico.colisionaCon(o)){
                quienes.add(o);
            }
        }
        return quienes;
    }
    
    public Escenario(int x, int y, int width, int height, JFrame marco) {
        setBounds(x, y, width, height);
        this.x = x;
        this.y = y;
        this.marco = marco;
        this.escalaX = (double) width / totalWidth;
        this.escalaY = (double) height / totalHeight;
        
        objetosGraficos= new ArrayList<>();
        objetosGraficos.add(new LlaveActual(240,180,20,20));
        objetosGraficos.add( new LlaveRoja(260,60,20,20) );
        //contadorLlave= new ContadorLlave(260,180,20,20);
        r_contador = new LlaveRoja(260,180,20,20);
        v_contador = new LlaveVerde(260,180,20,20);
        b_contador = new LlaveAzul(260,180,20,20);
        a_contador= new LlaveAmarilla(260,180,20,20);
        ricardo= new Ricardo(0,0,20,20, this, v_contador, b_contador,r_contador
        ,a_contador) ;

        objetosGraficos.add(r_contador);
        
        objetosGraficos.add(b_contador);
        objetosGraficos.add(a_contador);
        objetosGraficos.add(v_contador);
        
        a_contador.setVisible(false);
        r_contador.setVisible(false);
        v_contador.setVisible(false);
        b_contador.setVisible(false);
        
        marco.addKeyListener(ricardo);
        objetosGraficos.add(ricardo);
        objetosGraficos.add( new LlaveAzul(40,120,20,20) );
        objetosGraficos.add(new EdificioGris(240,120,20,20));        
        objetosGraficos.add(new EdificioGris(260,120,20,20));
        objetosGraficos.add( new LlaveVerde(0,40,20,20));
        objetosGraficos.add( new LlaveAmarilla(160,180,20,20));
        objetosGraficos.add( new EdificioAmarillo(220,100,20,20));
        objetosGraficos.add( new EdificioAzul(180,100,20,20));
        objetosGraficos.add( new EdificioVerde(80,0,20,20));
        objetosGraficos.add( new EdificioRojo(140,20,20,20));
        tiempoRestante= new TiempoRestante(240,160,20,20,this);
        Timer timer= new Timer();
        timer.scheduleAtFixedRate(tiempoRestante, 10, 1000);
        objetosGraficos.add( new Puntaje(240, 140, 20, 20));
        objetosGraficos.add( new Foras(20,0,20,20));
        objetosGraficos.add( new CasaRicardo(260,0,20,20));
        //objetosGraficos.add( new Eva(120,0,20,20,this));
        eva=new Eva(120,0,20,20,this);
        Thread threadEva=new Thread(eva);
        objetosGraficos.add(eva);
        threadEva.start();
        //int edificioGrisLength=60;
        //edificios = new EdificioGris[60];
        for (int i=0; i<10; i++){
            objetosGraficos.add(new EdificioGris(-20, i*20, 20, 20));
        }
        for (int i=0; i<10; i++){
            objetosGraficos.add(new EdificioGris(280, i*20, 20, 20));
        }
        for (int i=0; i<14; i++){
            objetosGraficos.add(new EdificioGris(i*20, -20, 20, 20));
        }
        for (int i=0; i<14; i++){
            objetosGraficos.add(new EdificioGris(i*20, 200, 20, 20));
        }
        for (int i=0; i<6;i++){
            //edificios[i]=new EdificioGris(beginX+i*20, beginY, 20,20);
            objetosGraficos.add(new EdificioGris(140+i*20, 0, 20,20));
        }
        //edificios[6]=new EdificioGris(0,20,20,20);
        objetosGraficos.add(new EdificioGris(0,20,20,20));
        //edificios[7]=new EdificioGris(20,20,20,20);
        objetosGraficos.add(new EdificioGris(20,20,20,20));
        
        for (int i=0; i<3; i++){
            //edificios[i+8]= new EdificioGris(60+i*20,20,20,20);
            objetosGraficos.add(new EdificioGris(60+i*20,20,20,20));
        }
        //edificios[11]=new EdificioGris(60,40,20,20);
        objetosGraficos.add(new EdificioGris(60,40,20,20));
        for (int i=0; i<4; i++){
            //edificios[12+i]=new EdificioGris(i*20,60,20,20);
            objetosGraficos.add(new EdificioGris(i*20,60,20,20));
        }
        for (int i=0; i<7; i++){
            //edificios[16+i]= new EdificioGris(140+i*20,40,20,20);
            objetosGraficos.add(new EdificioGris(140+i*20,40,20,20));
        }
        for (int i=0; i<5; i++){
            //edificios[23+i]=new EdificioGris(140+i*20, 60, 20, 20);
            objetosGraficos.add(new EdificioGris(140+i*20, 60, 20, 20));
        }
        //edificios[28]= new EdificioGris(180, 80, 20, 20);
        objetosGraficos.add(new EdificioGris(180, 80, 20, 20));
        //edificios[29]= new EdificioGris(220, 80, 20, 20);
        objetosGraficos.add(new EdificioGris(220, 80, 20, 20));
        for (int i=0; i<4; i++){
            //edificios[30+i]= new EdificioGris(220, 120+i*20, 20, 20);
            objetosGraficos.add(new EdificioGris(220, 120+i*20, 20, 20));
        }
        for (int i=0; i<4; i++){
            //edificios[34+i]= new EdificioGris(20+i*20,100, 20, 20);
            objetosGraficos.add(new EdificioGris(20+i*20,100, 20, 20));
        }
        //edificios[38]= new EdificioGris(120, 100, 20, 20);
        objetosGraficos.add(new EdificioGris(120, 100, 20, 20));
        //edificios[39]= new EdificioGris(140, 100, 20, 20);
        objetosGraficos.add(new EdificioGris(140, 100, 20, 20));
        
        //edificios[40]= new EdificioGris(20, 120, 20, 20);
        objetosGraficos.add(new EdificioGris(20, 120, 20, 20));
        //edificios[41]= new EdificioGris(80, 120, 20, 20);
        objetosGraficos.add(new EdificioGris(80, 120, 20, 20));
        //edificios[42]= new EdificioGris(180, 120, 20, 20);
        objetosGraficos.add(new EdificioGris(180, 120, 20, 20));
        //edificios[43]= new EdificioGris(220, 120, 20, 20);
        objetosGraficos.add(new EdificioGris(220, 120, 20, 20));
        
        //edificios[44]= new EdificioGris(20, 140, 20, 20);
        objetosGraficos.add(new EdificioGris(20, 140, 20, 20));
        //edificios[45]= new EdificioGris(40, 140, 20, 20);
        objetosGraficos.add(new EdificioGris(40, 140, 20, 20));
        
        for (int i=0; i<6; i++){
            //edificios[46+i]= new EdificioGris(80+i*20, 140, 20, 20);
            objetosGraficos.add(new EdificioGris(80+i*20, 140, 20, 20));
        }
        //edificios[52]= new EdificioGris(220, 140, 20, 20);
        objetosGraficos.add(new EdificioGris(220, 140, 20, 20));
        
        //edificios[53]= new EdificioGris(40, 160, 20, 20);
        objetosGraficos.add(new EdificioGris(40, 160, 20, 20));
        //edificios[54]= new EdificioGris(140, 160, 20, 20);
        objetosGraficos.add(new EdificioGris(140, 160, 20, 20));
        //edificios[55]= new EdificioGris(220, 160, 20, 20);
        objetosGraficos.add(new EdificioGris(220, 160, 20, 20));
        
        for (int i=0; i<4 ; i++){
            //edificios[56+i]= new EdificioGris(100+2*i*20, 180, 20, 20);
            objetosGraficos.add(new EdificioGris(100+2*i*20, 180, 20, 20));
        }
        //Para mover el protagonista
        //EscuchaTeclas escuchaTeclas = new EscuchaTeclas(ricardo, this);
        //marco.addKeyListener(escuchaTeclas);
        
    }
    
    @Override
    public void paint(Graphics g)
    {
        //Buffer
        Image imagenSegundoBuffer= createImage(marco.getWidth(), marco.getHeight());
        Graphics2D graphics2D = (Graphics2D) imagenSegundoBuffer.getGraphics();
        
        
        //Transformaciones
        AffineTransform affineTransform = graphics2D.getTransform();
        graphics2D.translate(x, y);
        graphics2D.scale(escalaX, escalaY);
        
        //Dibujar el protagonista
        //LlaveActual llaveActual = new LlaveActual(0,0, totalWidth /4.0d, totalHeight);
        //llaveActual.paint(graphics2D);
        
        //ricardo.paint(graphics2D);
        //eva.paint(graphics2D);
        //llaveAzul.paint(graphics2D);
        //llaveRoja.paint(graphics2D);
        //llaveActual.paint(graphics2D);
        //llaveVerde.paint(graphics2D);
        //llaveAmarilla.paint(graphics2D);
        //edificioAzul.paint(graphics2D);
        //edificioAmarillo.paint(graphics2D);
        //edificioVerde.paint(graphics2D);
        //edificioRojo.paint(graphics2D);
        tiempoRestante.paint(graphics2D);

        
        

        //puntaje.paint(graphics2D);
        //casaRicardo.paint(graphics2D);
        //foras.paint(graphics2D);
        for (ObjetoGrafico objetoGrafico : objetosGraficos){
            if (objetoGrafico.isVisible()){
                objetoGrafico.paint(graphics2D);
            }
        }
        
       // if (b_contador.isVisible()){
        //    b_contador.paint(graphics2D);
       // }
       // if (v_contador.isVisible()){
       //     v_contador.paint(graphics2D);
        //}
        //if (r_contador.isVisible()){
        //    r_contador.paint(graphics2D);
        //}
       // if (a_contador.isVisible()){
        //    a_contador.paint(graphics2D);
       // }
        
        //for (EdificioGris edificio : edificios){
        //    edificio.paint(graphics2D);
        //}
        
        
        //Si teneis problemas
        //Volver a la traslacion y escalacion anterior
        //graphics2D.setTransform(affineTransform);
        //Volver a la traslacion y escalacion anterior
        //new Grid(getTotalWidth(), getTotalHeight());
        graphics2D.setTransform(affineTransform);
        g.drawImage(imagenSegundoBuffer, 0,0, null);
    }
    
    @Override
    public void update (Graphics g){
        paint(g);
    }
}
