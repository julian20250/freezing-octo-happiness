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
    DisponiblesYVendidos actualizame;
    public BotonesBottom(MenuInmoviliariaK menu, DisponiblesYVendidos actualizame){
        this.menu=menu;
        this.actualizame=actualizame;
        setLayout(new GridLayout(1, 4));
        JButton btn1= new JButton("Dar Recaudo Neto");
        btn1.setActionCommand("Net");
        btn1.addActionListener(this);
        JButton btn2= new JButton("Dar Impuestos Pagados");
        btn2.setActionCommand("Pay");
        btn2.addActionListener(this);
        JButton btn3= new JButton("Dar Total Recaudo");
        btn3.setActionCommand("Recaudo");
        btn3.addActionListener(this);
        JButton btn4= new JButton("Vender of. más caras");
        btn4.setActionCommand("vender");
        btn4.addActionListener(this);
        add(btn1); add(btn2); add(btn3); add(btn4);
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
        }else if (e.getActionCommand().equals("vender")){
            try{
                sellMostExpensive();
            }catch(NotEnoughOfficesException ex){
                JOptionPane.showMessageDialog(new JFrame(), ex.getMessage());
            }
        }
    }

    private void sellMostExpensive() throws NotEnoughOfficesException {
        // How many offices are
        int numberOffices=0;
        for(Inmueble inmueble: menu.l)
            if(inmueble.getTipo()==1)
                numberOffices++;
        if(numberOffices<2)
            throw new NotEnoughOfficesException("Necesita al menos dos oficinas, tiene"
                    + " "+numberOffices+".");
        for(int ii=0; ii<2; ii++){
            int position=getMaxOfficePos();
            menu.venderInmueble(menu.l.get(position).getId());
        }
        actualizame.eraseMyself();
        actualizame.writeMyself();
    }

    private int getMaxOfficePos() {
        int count=0;
        int pos=0;
        double bestPrice=-1;
        for(Inmueble inmueble: menu.l){
            if(inmueble.getId()==1 && inmueble.getOriginalValue()>bestPrice)
                pos=count;
            count++;
        }
        return pos;
    }

    private static class NotEnoughOfficesException extends Exception {

        public NotEnoughOfficesException(String string) {
            super(string);
        }
    }
}
