/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package inmoviliariak;

import java.awt.GridLayout;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextField;

/**
 *
 * @author julian
 */
class Indicadores extends JPanel{
    
    private JLabel[] letras=new JLabel[]{
        new JLabel("ID"), new JLabel("Tipo"), new JLabel("Área"), 
        new JLabel("Estrato"), new JLabel("Valor"), new JLabel("Parqueadero"),
        new JLabel("# Parq."), new JLabel("Vigilancia"), new JLabel("Piso")
    };
    public Indicadores(MenuInmoviliariaK menu, JTextField[] campos){
        

        setLayout(new GridLayout(9,2));
        
        for (int ii=0; ii<9; ii++){
            add(letras[ii]);
            add(campos[ii]);
        }
        
    }

}
