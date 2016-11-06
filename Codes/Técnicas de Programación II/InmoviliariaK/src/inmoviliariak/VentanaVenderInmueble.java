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
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JTextArea;

/**
 *
 * @author julian
 */
class VentanaVenderInmueble extends JFrame implements ActionListener{
    private static JTextArea ID= new JTextArea();
    MenuInmoviliariaK menu;
    DisponiblesYVendidos actualizame;
    public VentanaVenderInmueble(MenuInmoviliariaK menu, DisponiblesYVendidos 
            actualizame){
        this.menu=menu;
        this.actualizame=actualizame;
        setSize(400, 200);
        setTitle("Vender Inmueble");
        JButton vender= new JButton("Vender");
        vender.addActionListener(this);
        vender.setActionCommand("vender");
        setLayout(new GridLayout(2, 2));
        add(new JLabel("Ingrese ID"));
        add(ID);
        add(vender);
        
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        if (e.getActionCommand().equals("vender")){
            menu.venderInmueble(Integer.parseInt(ID.getText()));
            actualizame.eraseMyself();
            actualizame.writeMyself();
            dispose();
        }
    }
}
