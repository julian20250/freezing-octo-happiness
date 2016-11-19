/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package inmoviliariak;

import java.awt.BorderLayout;
import java.awt.Image;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.ImageIcon;
import javax.swing.JFrame;
import javax.swing.JLabel;



/**
 *
 * @author julian
 */
public class Window extends JFrame implements ActionListener{
    MenuInmoviliariaK menu;
    public Window(MenuInmoviliariaK menu){
        this.menu=menu;
        setSize(900,600);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setTitle("Inmobiliaria K");
        setLayout(new BorderLayout());
        add(new JLabel(new ImageIcon(new ImageIcon("hero-enterprise.jpg").getImage().getScaledInstance(500, 100, Image.SCALE_DEFAULT))),
                BorderLayout.NORTH);
        DetalleInmueble detalleInmueble= new DetalleInmueble(menu);
        add(detalleInmueble, BorderLayout.WEST);
        DisponiblesYVendidos disponiblesYVendidos= new DisponiblesYVendidos(menu);
        add(disponiblesYVendidos, BorderLayout.EAST);
        BotonesBottom botonesBottom= new BotonesBottom(menu, disponiblesYVendidos);
        add(botonesBottom, BorderLayout.SOUTH); 
    }   
    
    @Override
    public void actionPerformed(ActionEvent e) {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }
    
}
