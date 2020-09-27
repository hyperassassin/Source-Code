//Quiz Test ---- Username :- student & Password :- admin ----
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import java.awt.Font;

public class quiz extends JFrame implements ActionListener
{
        JFrame f1,f2;
	JLabel l,l1,l2;
        JTextField t1;
        JPasswordField p1;
	JRadioButton jb[]=new JRadioButton[5];
	JButton b1,b2,b;
	ButtonGroup bg;
	int count=0,current=0,x=1,y=1,now=0;
	int m[]=new int[10];	
	public quiz()
	{   
                //LOGIN FRAME STARTS HERE
                f1=new JFrame(" Test ");
                f2=new JFrame(" Login ");
                l1=new JLabel(" Username : ");
                l2=new JLabel(" Password : ");
                p1=new JPasswordField(15);
                t1=new  JTextField(15);
                b=new JButton("Login");
                b.addActionListener(this);
                l1.setBounds(180,10,100,200);
                l1.setFont(new Font("Corbel",Font.PLAIN,14));
                l2.setBounds(180,75,100,200);
                l2.setFont(new Font("Corbel",Font.PLAIN,14));
                t1.setBounds(150,130,150,30);
                t1.setFont(new Font("Corbel",Font.PLAIN,14));
                p1.setBounds(150,190,150,30);
                b.setBounds(170,230,100,30); 
                b.setFont(new Font("Corbel",Font.PLAIN,14));
                f2.setLayout(null);
                f2.add(l1);
                f2.add(t1);
                f2.add(l2);
                f2.add(p1);
                f2.add(b);
                f2.getContentPane().setBackground(Color.WHITE);
                f2.setSize(500,350);
                f2.setVisible(true);
                //LOGIN FRAME ENDS HERE
                
		l=new JLabel();
		f1.add(l);
		bg=new ButtonGroup();
		for(int i=0;i<5;i++)
		{
			jb[i]=new JRadioButton();	
			f1.add(jb[i]);
			bg.add(jb[i]);
                        jb[i].setBackground(Color.WHITE);
		}
		b1=new JButton("Next");
                b1.setFont(new Font("Corbel",Font.PLAIN,14));
		b2=new JButton("Bookmark");
                b2.setFont(new Font("Corbel",Font.PLAIN,12));
		b1.addActionListener(this);
		b2.addActionListener(this);
		f1.add(b1);f1.add(b2);
		set();
		l.setBounds(30,40,450,20);
                l.setFont(new Font("Comic Sans MS",Font.PLAIN,14));
		jb[0].setBounds(50,80,100,20);
                jb[0].setFont(new Font("Corbel",Font.PLAIN,14));
		jb[1].setBounds(50,110,100,20);
                jb[1].setFont(new Font("Corbel",Font.PLAIN,14));
		jb[2].setBounds(50,140,100,20);
                jb[2].setFont(new Font("Corbel",Font.PLAIN,14));
		jb[3].setBounds(50,170,100,20);
                jb[3].setFont(new Font("Corbel",Font.PLAIN,14));
		b1.setBounds(100,240,100,30);
		b2.setBounds(270,240,100,30);
		f1.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		f1.setLayout(null);
                f1.getContentPane().setBackground(Color.WHITE);
		f1.setSize(650,350);
	}
	public void actionPerformed(ActionEvent e)
	{
                if(e.getSource()==b)
                {
                    String s =t1.getText();
                    String a= p1.getText();
                    if(s.equals("student")&& a.equals("admin"))
                    {
                        f2.setVisible(false);
                        f1.setVisible(true);
                    }
                }
		if(e.getSource()==b1)
		{
			if(check())
				count=count+1;
			current++;
			set();	
			if(current==9)
			{
				b1.setEnabled(false);
				b2.setText("Result");
			}
		}
		if(e.getActionCommand().equals("Bookmark"))
		{
			JButton bk=new JButton("Bookmark"+x);
			bk.setBounds(480,20+30*x,100,30);
			f1.add(bk);
			bk.addActionListener(this);
			m[x]=current;
			x++;
			current++;
			set();	
			if(current==9)
				b2.setText("Result");
			f1.setVisible(false);
			f1.setVisible(true);
		}
		for(int i=0,y=1;i<x;i++,y++)
		{
		if(e.getActionCommand().equals("Bookmark"+y))
		{
			if(check())
				count=count+1;
			now=current;
			current=m[y];
			set();
			((JButton)e.getSource()).setEnabled(false);
			current=now;
		}
		}
	
		if(e.getActionCommand().equals("Result"))
		{
			if(check())
				count=count+1;
			current++;
			//System.out.println("correct ans="+count);
			JOptionPane.showMessageDialog(this,"Your Score :- "+count);
			System.exit(0);
		}
	}
	void set()
	{
            jb[4].setSelected(true);  
        if(current==0)  
        {  
            l.setText("Q.1: Which one among these is not a primitive datatype?");  
            jb[0].setText(" int ");jb[1].setText(" Float ");jb[2].setText(" boolean ");jb[3].setText(" char ");   
        }  
        if(current==1)  
        {  
            l.setText("Q.2: Which class is available to all the class automatically?");  
            jb[0].setText(" Swing ");jb[1].setText(" Applet ");jb[2].setText(" Object ");jb[3].setText(" ActionEvent ");  
        }  
        if(current==2)  
        {  
            l.setText("Q.3: What is the range of short data type in Java?");  
            jb[0].setText(" -128 to 127 ");jb[1].setText(" -32768 to 32767 ");jb[2].setText(" -2147483648 to 2147483647 ");jb[3].setText(" None of the mentioned ");  
        }  
        if(current==3)  
        {  
            l.setText("Q.4: String class is defined in which package?");  
            jb[0].setText(" lang ");jb[1].setText(" Swing ");jb[2].setText(" Applet ");jb[3].setText(" awt ");  
        }  
        if(current==4)  
        {  
            l.setText("Q.5: Which keywords is not a part of exception handling?");  
            jb[0].setText(" try ");jb[1].setText(" Catch ");jb[2].setText(" thrown ");jb[3].setText(" finally ");  
        }  
        if(current==5)  
        {  
            l.setText("Q.6: Which of these are selection statements in Java? ");  
            jb[0].setText(" if ");jb[1].setText(" for ");jb[2].setText(" continue ");jb[3].setText(" break ");  
        }  
        if(current==6)  
        {  
            l.setText("Q.7: Which packages contain all the Java’s built in exceptions? ");  
            jb[0].setText(" java.io ");jb[1].setText(" java.util ");jb[2].setText(" java.lang ");jb[3].setText(" java.net ");  
        }  
        if(current==7)  
        {  
            l.setText("Q.8: Which of the following is not a Java features? ");  
            jb[0].setText(" Dynamic ");jb[1].setText(" Architecture Neutral ");jb[2].setText(" Use of pointers ");jb[3].setText(" Object-oriented ");         
        }  
        if(current==8)  
        {  
            l.setText("Q.9: Which function is not present in Applet class?");  
            jb[0].setText(" init ");jb[1].setText(" main ");jb[2].setText(" start ");jb[3].setText(" destroy ");  
        }  
        if(current==9)  
        {  
            l.setText("Q.10: Which one among these is not a valid component?");  
            jb[0].setText(" JButton ");jb[1].setText(" JList ");jb[2].setText(" JButtonGroup ");jb[3].setText(" JTextArea ");  
        }  
        l.setBounds(30,40,450,20);  
        for(int i=0,j=0;i<=90;i+=30,j++)  
            jb[j].setBounds(50,80+i,200,20);  
	}
	boolean check()
	{
		if(current==0)
			return(jb[1].isSelected());
		if(current==1)
			return(jb[2].isSelected());
		if(current==2)
			return(jb[1].isSelected());
		if(current==3)
			return(jb[0].isSelected());
		if(current==4)
			return(jb[2].isSelected());
		if(current==5)
			return(jb[0].isSelected());
		if(current==6)
			return(jb[2].isSelected());
		if(current==7)
			return(jb[2].isSelected());
		if(current==8)
			return(jb[1].isSelected());
		if(current==9)
			return(jb[2].isSelected());
		return true;
	}
	public static void main(String s[])
	{
		new quiz();
	}
}
