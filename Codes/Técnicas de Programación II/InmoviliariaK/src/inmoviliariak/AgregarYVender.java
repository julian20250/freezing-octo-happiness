/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package inmoviliariak;

import java.awt.Frame;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.JButton;
import javax.swing.JOptionPane;
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
        setLayout(new GridLayout(1, 3));
        JButton agregar = new JButton("Agregar");
        agregar.setActionCommand("Agregar");
        agregar.addActionListener(this);
        JButton vender = new JButton("Vender");
        vender.setActionCommand("Vender");
        vender.addActionListener(this);
        JButton recuperar = new JButton("Recuperar Vendidos");
        recuperar.setActionCommand("recuperar");
        recuperar.addActionListener(this);
        add(agregar);add(vender); add(recuperar);
    }

    public void restoreSelled() throws RepeadetIDException{
        int [] listOfID=new int[menu.l.size()];
        boolean anyRepeated=false;
        int count=0;
        for(Inmueble inmueble: menu.l){
            listOfID[count]=inmueble.getId();
        }
        for (int ii=0; ii<listOfID.length; ii++)
            for(Inmueble inmueble: menu.V)
                if(inmueble.getId()==listOfID[ii])
                    anyRepeated=true;
        if(anyRepeated)
            throw new RepeadetIDException("Hay dos inmuebles, uno en los vendidos"
                    + " y otro en los disponibles con el mismo ID,"
                    + " por lo que no se puede recuperar");
        for(Inmueble inmueble: menu.V)
            menu.l.add(inmueble);
        menu.V.clear();                    
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
        }else if(e.getActionCommand().equals("recuperar")){
            try{
                restoreSelled();
                actualizame.eraseMyself();
                actualizame.writeMyself();
            }
            catch(RepeadetIDException ex){
                JOptionPane.showMessageDialog(new Frame(), ex.getMessage());
            }
        }
    }

    private static class RepeadetIDException extends Exception {

        public RepeadetIDException(String string) {
            super(string);
        }
    }
}
