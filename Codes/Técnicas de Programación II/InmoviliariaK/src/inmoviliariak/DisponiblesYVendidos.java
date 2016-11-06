/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package inmoviliariak;

import java.awt.GridLayout;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;

/**
 *
 * @author julian
 */
public class DisponiblesYVendidos extends JPanel{
    private JTextArea disponibles= new JTextArea(10, 10);
    private JTextArea vendidos= new JTextArea(10, 10);
    MenuInmoviliariaK menu;
    public DisponiblesYVendidos(MenuInmoviliariaK menu){
        disponibles.setEditable(false);
        vendidos.setEditable(false);
        this.menu=menu;
        
        JScrollPane sc1= new JScrollPane(disponibles);
        JScrollPane sc2= new JScrollPane(vendidos);
        setLayout(new GridLayout(5, 1));
        add(new JLabel("Inmuebles Disponibles"));
        add(sc1);
        add(new JLabel("Inmuebles Vendidos"));
        add(sc2);
        AgregarYVender agregarYVender = new AgregarYVender(menu, this);
        add(agregarYVender);
    }
    public void writeMyself(){
        for (Inmueble inmueble: menu.l)
            disponibles.append(""+inmueble.getId()+"\n");
        for (Inmueble inmueble: menu.V)
            vendidos.append(""+inmueble.getId()+"\n");
    }
    public void eraseMyself(){
        disponibles.setText(null);
        vendidos.setText(null);
    }
}
