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
import javax.swing.JOptionPane;
import javax.swing.JPanel;

/**
 *
 * @author julian
 */
public class BotonesBottom extends JPanel implements ActionListener{
    MenuInmoviliariaK menu;
    public BotonesBottom(MenuInmoviliariaK menu){
        this.menu=menu;
        setLayout(new GridLayout(1, 3));
        JButton btn1= new JButton("Dar Recaudo Neto");
        btn1.setActionCommand("Net");
        btn1.addActionListener(this);
        JButton btn2= new JButton("Dar Impuestos Pagados");
        btn2.setActionCommand("Pay");
        btn2.addActionListener(this);
        JButton btn3= new JButton("Dar Total Recaudo");
        btn3.setActionCommand("Recaudo");
        btn3.addActionListener(this);
        add(btn1); add(btn2); add(btn3);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        if(e.getActionCommand().equals("Net")){
            JOptionPane.showMessageDialog(new JFrame(),  menu.darRecaudoNeto());
        }else if(e.getActionCommand().equals("Pay")){
            try{
                JOptionPane.showMessageDialog(new JFrame(),  menu.darImpuestosPagados());
            }catch(CeroInmueblesVendidosException ex){
                JOptionPane.showMessageDialog(new JFrame(),  ex.getMessage());
            }
        }else if (e.getActionCommand().equals("Recaudo")){
            JOptionPane.showMessageDialog(new JFrame(),  menu.darRecaudosDespuesDeImpuestos());
        }
    }
}
