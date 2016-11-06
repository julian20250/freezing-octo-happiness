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
import javax.swing.JPanel;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JTextField;

/**
 *
 * @author julian
 */
public class VentanaAgregarInmueble extends JFrame implements ActionListener{
    private static JTextField[] campos=new JTextField[]{
        new JTextField(""), new JTextField(""),
        new JTextField(""), new JTextField(""),
        new JTextField(""), new JTextField(""),
        new JTextField(""), new JTextField(""), new JTextField("")
    };
    MenuInmoviliariaK menu;
    DisponiblesYVendidos actualizame;
    public VentanaAgregarInmueble(MenuInmoviliariaK menu, DisponiblesYVendidos actualizame){
        this.actualizame=actualizame;
        this.menu=menu;
        setTitle("Agregar Inmueble");
        setSize(500,600);
        setLayout(new GridLayout(3, 1));
        add(new JLabel("Nota: Sólo se leerán los campos correspondientes a cada"
                + " inmueble."));
        InterfaceToAdd interfaceToAdd = new InterfaceToAdd();
        add(interfaceToAdd);
        JButton aceptar= new JButton("Aceptar");
        aceptar.addActionListener(this);
        aceptar.setActionCommand("Aceptar");
        add(aceptar);
        
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        if (e.getActionCommand().equals("Aceptar")){
            try{
                menu.agregarInmueble(fragments());
                actualizame.eraseMyself();
                actualizame.writeMyself();
                dispose();
                
            }
            catch(NumeroInadecuadoDeParametrosException ex){
                JOptionPane.showMessageDialog(new JFrame(),  ex.getMessage());
            }catch(MuchasOficinasException ex){
                JOptionPane.showMessageDialog(new JFrame(),  ex.getMessage());
            }catch(IdentificadorRepetidoException ex){
                JOptionPane.showMessageDialog(new JFrame(),  ex.getMessage());
            }catch(NoIngresoBooleanException ex){
                JOptionPane.showMessageDialog(new JFrame(),  ex.getMessage());
            }catch(TipoDesconocidoException ex){
                JOptionPane.showMessageDialog(new JFrame(),  ex.getMessage());
            }
        }
    }

    private String fragments() throws TipoDesconocidoException{
        String str="";
        if (campos[1].getText().equals("1")){
            str=campos[0].getText()+"-"+campos[1].getText()+"-"+campos[2].getText()+"-"+
                    campos[3].getText()+"-"+campos[4].getText()+"-"+campos[5].getText();
        }else if(campos[1].getText().equals("2")){
            str=campos[0].getText()+"-"+campos[1].getText()+"-"+campos[2].getText()+"-"+
                    campos[3].getText()+"-"+campos[4].getText()+"-"+campos[6].getText()
                    +"-"+campos[7].getText();
        }else if(campos[1].getText().equals("3")){
            str=campos[0].getText()+"-"+campos[1].getText()+"-"+campos[2].getText()+"-"+
                    campos[3].getText()+"-"+campos[4].getText()+"-"+campos[6].getText()+"-"+
                    campos[8].getText();
        }else{
            throw new TipoDesconocidoException(campos[1].getText()+" no es un ti"
                    + "po de dato válido.");
        }
        
        return str;
    }

    private static class InterfaceToAdd extends JPanel{
        private static JLabel[] labels={
            new JLabel("ID"), new JLabel("Tipo"), new JLabel("Metros"
                    + " Cuadrados"), new JLabel("Estrato"),
            new JLabel("Valor Base Metro Cuadrado"), new JLabel("Parquea"
                    + "dero Visitante"), new JLabel("n"
                            + "úmero Parqueaderos"), new JLabel("Vigilancia "
                                    + "Privada"), new JLabel("Piso")
        };
        
        public InterfaceToAdd(){
            setLayout(new GridLayout(9, 2));        
            for (int ii=0; ii<9; ii++){
                add(labels[ii]);
                add(campos[ii]);
            }
        }
    }
}
