/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package inmoviliariak;

import java.awt.BorderLayout;
import java.awt.Image;
import javax.swing.ImageIcon;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextField;

/**
 *
 * @author julian
 */
public class DetalleInmueble extends JPanel{
    MenuInmoviliariaK menu;
    private JTextField[] campos= new JTextField[9];
    private JLabel imageLabel= new JLabel(new ImageIcon(new ImageIcon("hero-enterprise.jpg").getImage().getScaledInstance(100, 50, Image.SCALE_DEFAULT)));
    ImageIcon[] photos = new ImageIcon[]{
      new ImageIcon(new ImageIcon("hero-enterprise.jpg").getImage().getScaledInstance(100, 50, Image.SCALE_DEFAULT)), 
        new ImageIcon(new ImageIcon("office.jpeg").getImage().getScaledInstance(100, 50, Image.SCALE_DEFAULT)),
        new ImageIcon(new ImageIcon("house.jpg").getImage().getScaledInstance(100, 50, Image.SCALE_DEFAULT)), 
        new ImageIcon(new ImageIcon("appartment.jpg").getImage().getScaledInstance(100, 50, Image.SCALE_DEFAULT))             
    };
    public DetalleInmueble(MenuInmoviliariaK menu){
        for (int ii=0; ii<9; ii++){
            campos[ii]=new JTextField("Presione siguiente"); 
            campos[ii].setEditable(false);
        }
        campos[2].setText("Al ingresar");
        campos[3].setText("Inmueble");
        this.menu=menu;
        setLayout(new BorderLayout());
        add(new JLabel("Detalle Inmueble"), BorderLayout.NORTH);
        add(imageLabel,
        BorderLayout.WEST);
        Indicadores indicadores= new Indicadores(menu, campos);
        add(indicadores, BorderLayout.EAST);
        BotonesDetalle botonesDetalle= new BotonesDetalle(campos, menu,imageLabel,photos);
        add(botonesDetalle, BorderLayout.SOUTH);
    }
}
