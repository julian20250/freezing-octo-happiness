/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package inmoviliariak;

import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.JButton;
import javax.swing.JPanel;

/**
 *
 * @author julian
 */
class AgregarYVender extends JPanel implements ActionListener{
    MenuInmoviliariaK menu;
    DisponiblesYVendidos actualizame;
    public AgregarYVender(MenuInmoviliariaK menu, DisponiblesYVendidos actualizame){
        this.actualizame=actualizame;
        this.menu=menu;
        setLayout(new GridLayout(1, 2));
        JButton agregar = new JButton("Agregar");
        agregar.setActionCommand("Agregar");
        agregar.addActionListener(this);
        JButton vender = new JButton("Vender");
        vender.setActionCommand("Vender");
        vender.addActionListener(this);
        add(agregar);add(vender);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        if (e.getActionCommand().equals("Agregar")){
            VentanaAgregarInmueble ventanaAgregarInmueble;
            ventanaAgregarInmueble= new VentanaAgregarInmueble(menu, actualizame);
            ventanaAgregarInmueble.setVisible(true);
        }else if(e.getActionCommand().equals("Vender")){
            VentanaVenderInmueble ventanaVenderInmueble;
            ventanaVenderInmueble= new VentanaVenderInmueble(menu, actualizame);
            ventanaVenderInmueble.setVisible(true);
        }        
    }
}
