import java.awt.event.*;
import java.awt.Color;
import javax.swing.*;
public class puzzle_game_java extends JFrame implements ActionListener 
{
    JButton b1,b2,b3,b4,b5,b6,b7,b8,b9;
    JLabel l,l1;
    JFrame f1;
    
    public puzzle_game_java()
    {
        //Components..
        f1 = new JFrame("Puzzle Game..");
        l = new JLabel("Welcome To The Puzzle Game. !!"); 
        l1 = new JLabel("You Have To Arrange The Numbers In Correct Order.");
        l.setBounds(30,-110,300,300);
        l1.setBounds(30,-90,300,300);
        b1 = new JButton("1");
        b2 = new JButton("2");
        b3 = new JButton("3");
        b4 = new JButton("4");
        b5 = new JButton("5");
        b6 = new JButton("6");
        b7 = new JButton("7");
        b8 = new JButton("");
        b9 = new JButton("8");
        
        // Setting Background Color..
        b1.setBackground(Color.WHITE);
        b2.setBackground(Color.WHITE);
        b3.setBackground(Color.WHITE);
        b4.setBackground(Color.WHITE);
        b5.setBackground(Color.WHITE);
        b6.setBackground(Color.WHITE);
        b7.setBackground(Color.WHITE);
        b8.setBackground(Color.WHITE);
        b9.setBackground(Color.WHITE);
        
        //Adding Action Listener To The Button..
        b1.addActionListener(this);
        b2.addActionListener(this);
        b3.addActionListener(this);
        b4.addActionListener(this);
        b5.addActionListener(this);
        b6.addActionListener(this);
        b7.addActionListener(this);
        b8.addActionListener(this);
        b9.addActionListener(this);
        
        //Setting The Bounds For The Components..
        b1.setBounds(50,100,50,40);
        b2.setBounds(100,100,50,40);
        b3.setBounds(150,100,50,40);
        b4.setBounds(50,150,50,40);
        b5.setBounds(100,150,50,40);
        b6.setBounds(150,150,50,40);
        b7.setBounds(50,200,50,40);
        b8.setBounds(100,200,50,40);
        b9.setBounds(150,200,50,40);
        
        //Adding All The Components To The Frame..
        f1.add(l);
        f1.add(l1);
        f1.add(b1);
        f1.add(b2);
        f1.add(b3);
        f1.add(b4);
        f1.add(b5);
        f1.add(b6);
        f1.add(b7);
        f1.add(b8);
        f1.add(b9);
        f1.getContentPane().setBackground(Color.WHITE);
        f1.setLayout(null);
        f1.setSize(400,400);
        f1.setVisible(true);
    }
     @Override
    public void actionPerformed(ActionEvent e) 
    {
        if(e.getSource()== b1)
        {
            String l = b1.getLabel();
            if(b2.getLabel().equals(""))
            {
                b2.setLabel(l);
                b1.setLabel("");
            }
            if(b4.getLabel().equals(""))
            {
                b4.setLabel(l);
                b4.setLabel("");   
            }
        }
        if(e.getSource()== b2)
        {
            String l = b2.getLabel();
            if(b1.getLabel().equals(""))
            {
                b1.setLabel(l);
                b2.setLabel("");
            }
            if(b3.getLabel().equals(""))
            {
                b3.setLabel(l);
                b2.setLabel("");
            }
            if(b5.getLabel().equals(""))
            {
                b5.setLabel(l);
                b2.setLabel("");
            } 
        }
        if(e.getSource()== b3)
        {
            String l = b3.getLabel();
            if(b2.getLabel().equals(""))
            {
                b2.setLabel(l);
                b3.setLabel("");
            }
            if(b6.getLabel().equals(""))
            {
                b6.setLabel(l);
                b3.setLabel("");
            }
        }
        if(e.getSource()== b4)
        {
            String l = b4.getLabel();
            if(b1.getLabel().equals(""))
            {
                b1.setLabel(l);
                b4.setLabel("");
            }
            if(b7.getLabel().equals(""))
            {
                b7.setLabel(l);
                b4.setLabel("");
            }
            if(b5.getLabel().equals(""))
            {
                b5.setLabel(l);
                b4.setLabel("");
            }
        }
        if(e.getSource()== b5)
        {
            String l = b5.getLabel();
            if(b2.getLabel().equals(""))
            {
                b2.setLabel(l);
                b5.setLabel("");
            }
            if(b6.getLabel().equals(""))
            {
                b6.setLabel(l);
                b5.setLabel("");
            }
            if(b4.getLabel().equals(""))
            {
                b4.setLabel(l);
                b5.setLabel("");
            }
            if(b8.getLabel().equals(""))
            {
                b8.setLabel(l);
                b5.setLabel("");
            }
        }
        if(e.getSource()== b6)
        {
            String l = b6.getLabel();
            if(b9.getLabel().equals(""))
            {
                b9.setLabel(l);
                b6.setLabel("");
            }
            if(b3.getLabel().equals(""))
            {
                b3.setLabel(l);
                b6.setLabel("");
            }
            if(b5.getLabel().equals(""))
            {
                b5.setLabel(l);
                b6.setLabel("");
            }
        }
        if(e.getSource()== b7)
        {
            String l = b7.getLabel();
            if(b4.getLabel().equals(""))
            {
                b4.setLabel(l);
                b7.setLabel("");
            }
            if(b8.getLabel().equals(""))
            {
                b8.setLabel(l);
                b7.setLabel("");
            }
        }
        if(e.getSource()== b8)
        {
            String l = b8.getLabel();
            if(b9.getLabel().equals(""))
            {
                b9.setLabel(l);
                b8.setLabel("");
            }
            if(b7.getLabel().equals(""))
            {
                b7.setLabel(l);
                b8.setLabel("");
            }
            if(b5.getLabel().equals(""))
            {
                b5.setLabel(l);
                b8.setLabel("");
            }
        }
        if(e.getSource()== b9)
        {
            String l = b9.getLabel();
            if(b6.getLabel().equals(""))
            {
                b6.setLabel(l);
                b9.setLabel("");
            }
            if(b8.getLabel().equals(""))
            {
                b8.setLabel(l);
                b9.setLabel("");
            }
        }
        if(b1.getLabel().equals("1") && b2.getLabel().equals("2") && b3.getLabel().equals("3") && b4.getLabel().equals("4") && b5.getLabel().equals("5") && b6.getLabel().equals("6") && b7.getLabel().equals("7") && b8.getLabel().equals("8") && b9.getLabel().equals(""))
        {
            JOptionPane.showMessageDialog(this, "Congrats!! You Won The Game! ");
        }        
    }
    public static void main(String[]args)
    {
        new puzzle_game_java();
    }
}
