//Mysql Connector Should be Installed Before Running the Project.
//Username :- admin & Password :- admin
import java.awt.Color;
import java.awt.Font;
import java.awt.HeadlessException;
import javax.swing.*;
import java.awt.event.*;
import java.sql.*;
public class inventory extends JFrame implements ActionListener
{
    JFrame f1,f2,f3,f4,f5,f6;
    JLabel l,l1,l2,id,name,quan,type,desc,i1,s1,sw,uid,uname,uquan,utype,udesc,la;
    JTextField t,itxt,ntxt,qtxt,ytxt,dtxt,idel,stxt,utxt,ptxt,atxt,mtxt,etxt;
    JPasswordField p1;
    JButton b,b1,b2,b3,b4,add,del,search,update,c1,c2,cl1,cl2,cl3,cl4;
    
    public inventory()
    {
        //LOGIN FRAME 
        f1 = new JFrame("LOGIN");
        l = new JLabel("Username :- ");
        l1 = new JLabel("Password :- ");
        t = new JTextField(20);
        p1 = new JPasswordField(15);
        b = new JButton("Login");
        c1 = new JButton("Close");
        b.addActionListener(this);
        c1.addActionListener(this);
        l.setBounds(180,10,100,200);
        l1.setBounds(180,75,100,200);
        t.setBounds(150,130,150,30);
        p1.setBounds(150,190,150,30);
        b.setBounds(140,230,80,30);
        c1.setBounds(240,230,80,30);
        f1.add(l);f1.add(l1);f1.add(t);f1.add(p1);f1.add(b);f1.add(c1);
        f1.setLayout(null);
        f1.getContentPane().setBackground(Color.WHITE);
        f1.setSize(500,350);
        f1.setVisible(true);
        //END
        
        //MAIN FRAME
        f2 = new JFrame("INVENTORY");
        l2 = new JLabel(" INVENTORY ");
        l2.setFont(new Font("Comic Sans MS",Font.PLAIN,48));
        b1 = new JButton("Add Product");
        b2 = new JButton("Update Product");
        b3 = new JButton("Search Product");
        b4 = new JButton("Delete Product");
        c2 = new JButton("Close");
        c2.addActionListener(this);
        b1.addActionListener(this);
        b2.addActionListener(this);
        b3.addActionListener(this);
        b4.addActionListener(this);
        l2.setBounds(120,40,400,50);
        b1.setBounds(10,150,150,30);
        b2.setBounds(10,250,150,30);
        b3.setBounds(400,150,150,30);
        b4.setBounds(400,250,150,30);
        c2.setBounds(230,280,70,30);
        f2.add(l2);f2.add(b1);f2.add(b2);f2.add(b3);f2.add(b4);f2.add(c2);
        f2.setLayout(null);
        f2.getContentPane().setBackground(Color.WHITE);
        f2.setSize(580,350);
        //f2.setVisible(true);
        //END
        
        //ADD PRODUCT FRAME
        f3 = new JFrame("ADD PRODUCT");
        id = new JLabel(" Item Id :- ");
        name = new JLabel(" Item Name :- ");
        quan = new JLabel(" Quantity :- ");
        type = new JLabel(" Type Of Product :- ");
        desc = new JLabel(" Description :- ");
        id.setFont(new Font("Comic Sans MS",Font.BOLD,14));
        name.setFont(new Font("Comic Sans MS",Font.BOLD,14));
        quan.setFont(new Font("Comic Sans MS",Font.BOLD,14));
        type.setFont(new Font("Comic Sans MS",Font.BOLD,11));
        desc.setFont(new Font("Comic Sans MS",Font.BOLD,14));
        itxt = new JTextField(10);
        ntxt = new JTextField(30);
        qtxt = new JTextField(10);
        ytxt = new JTextField(30);
        dtxt = new JTextField(50);
        add = new JButton("Add Item");
        cl1 = new JButton("Close");
        add.addActionListener(this);
        cl1.addActionListener(this);
        id.setBounds(20,50,150,50);
        name.setBounds(20,100,150,50);
        quan.setBounds(20,150,150,50);
        type.setBounds(20,200,150,50);
        desc.setBounds(20,250,150,50);
        itxt.setBounds(130,60,100,30);
        ntxt.setBounds(130,110,100,30);
        qtxt.setBounds(130,160,100,30);
        ytxt.setBounds(130,210,100,30);
        dtxt.setBounds(130,260,100,30);
        add.setBounds(20,310,100,30);
        cl1.setBounds(140,310,70,30);
        f3.add(id);f3.add(name);f3.add(quan);f3.add(type);f3.add(desc);
        f3.add(itxt);f3.add(ntxt);f3.add(qtxt);f3.add(ytxt);f3.add(dtxt);f3.add(add);f3.add(cl1);
        f3.setLayout(null);
        f3.getContentPane().setBackground(Color.WHITE);
        f3.setSize(400,400);
        f3.setVisible(false);
        //END
        
        //DELETE PRODUCT FRAME
        f4 = new JFrame("DELETE PRODUCT");
        i1 = new JLabel("Item Id :- ");
        i1.setFont(new Font("Comic Sans MS",Font.BOLD,14));
        idel = new JTextField(10);
        del = new JButton("Delete Item");
        cl4 = new JButton("Close");
        del.addActionListener(this);
        cl4.addActionListener(this);
        i1.setBounds(20,50,150,50);
        idel.setBounds(130,60,100,30);
        del.setBounds(40,120,100,30);
        cl4.setBounds(160,120,70,30);
        f4.add(i1);f4.add(idel);f4.add(del);f4.add(cl4);
        f4.setLayout(null);
        f4.getContentPane().setBackground(Color.WHITE);
        f4.setSize(400,400);
        f4.setVisible(false);
        
        //SEARCH PRODUCT FRAME
        f5 = new JFrame("SEARCH PRODUCT");
        s1 = new JLabel("Item Id :- ");
        s1.setFont(new Font("Comic Sans MS",Font.BOLD,14));
        la = new JLabel("  ID       |       NAME        |     QUANTITY      |       TYPE        |        DESCRIPTION       |");
        sw = new JLabel(" "); 
        stxt = new JTextField(10);
        search = new JButton("Search Item");
        cl3 = new JButton("Close");
        search.addActionListener(this);
        cl3.addActionListener(this);
        s1.setBounds(20,50,150,50);
        stxt.setBounds(130,60,100,30);
        search.setBounds(40,120,110,30);
        cl3.setBounds(160,120,70,30);
        la.setBounds(20,140,600,100);
        sw.setBounds(22,170,600,100);
        f5.add(s1);f5.add(stxt);f5.add(search);f5.add(la);f5.add(sw);f5.add(cl3);
        f5.setLayout(null);
        f5.getContentPane().setBackground(Color.WHITE);
        f5.setSize(440,400);
        f5.setVisible(false);  
        
        //UPDATE PRODUCT FRAME
        f6 = new JFrame("UPDATE PRODUCT");
        uid = new JLabel(" Item Id :- ");
        uname = new JLabel(" Item Name :- ");
        uquan = new JLabel(" Quantity :- ");
        utype = new JLabel(" Type Of Product :- ");
        udesc = new JLabel(" Description :- ");
        uid.setFont(new Font("Comic Sans MS",Font.BOLD,14));
        uname.setFont(new Font("Comic Sans MS",Font.BOLD,14));
        uquan.setFont(new Font("Comic Sans MS",Font.BOLD,14));
        utype.setFont(new Font("Comic Sans MS",Font.BOLD,11));
        udesc.setFont(new Font("Comic Sans MS",Font.BOLD,14));
        utxt = new JTextField(10);
        ptxt = new JTextField(30);
        atxt = new JTextField(10);
        mtxt = new JTextField(30);
        etxt = new JTextField(50);
        update = new JButton("Update Item");
        cl2 = new JButton("Close");
        update.addActionListener(this);
        cl2.addActionListener(this);
        uid.setBounds(20,50,150,50);
        uname.setBounds(20,100,150,50);
        uquan.setBounds(20,150,150,50);
        utype.setBounds(20,200,150,50);
        udesc.setBounds(20,250,150,50);
        utxt.setBounds(130,60,100,30);
        ptxt.setBounds(130,110,100,30);
        atxt.setBounds(130,160,100,30);
        mtxt.setBounds(130,210,100,30);
        etxt.setBounds(130,260,100,30);
        update.setBounds(20,310,110,30);
        cl2.setBounds(160,310,70,30);
        f6.add(uid);f6.add(uname);f6.add(uquan);f6.add(utype);f6.add(udesc);
        f6.add(utxt);f6.add(ptxt);f6.add(atxt);f6.add(mtxt);f6.add(etxt);f6.add(update);f6.add(cl2);
        f6.setLayout(null);
        f6.getContentPane().setBackground(Color.WHITE);
        f6.setSize(400,400);
        f6.setVisible(false);
    }
    @Override
    public void actionPerformed(ActionEvent ae)
    {
        if(ae.getSource()== b)
        {
            String a = t.getText();
            String b = p1.getText();
            if(a.equals("admin") && b.equals("admin"))
            {
                f1.setVisible(false);
                f2.setVisible(true);
            }
            else
            {
                int type = JOptionPane.ERROR_MESSAGE;
                String msg = "Invalid Username Or Password";
                JOptionPane.showMessageDialog(null,msg,"Error",type);
            }
        }
        if(ae.getSource()== c1)
        {
            f1.setVisible(false);
            System.exit(0);
        }
        if(ae.getSource()== c2)
        {
            f2.setVisible(false);
            System.exit(0);
        }
        if(ae.getSource()== cl1)
        {
            f3.setVisible(false);
            f2.setVisible(true);
            itxt.setText("");
            ntxt.setText("");
            qtxt.setText("");
            ytxt.setText("");
            dtxt.setText("");
        }
        if(ae.getSource()== b1)
        {
            f3.setVisible(true);
            f2.setVisible(false);
        }
        if(ae.getSource()== add)
        {
            try
            {
                Class.forName("com.mysql.jdbc.Driver");
                Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:33060/inventory","root","sagar");
                String sql = "insert into stock values(?,?,?,?,?)";
                PreparedStatement pstmt = conn.prepareStatement(sql);
                int r1 = Integer.parseInt(itxt.getText());
                pstmt.setString(1,itxt.getText());
                pstmt.setString(2,ntxt.getText());
                pstmt.setString(3,qtxt.getText());
                pstmt.setString(4,ytxt.getText());
                pstmt.setString(5,dtxt.getText());
                JOptionPane.showMessageDialog(this,"Product "+r1+" Added Successfully");
                pstmt.executeUpdate();
                pstmt.close();
            }
            catch(ClassNotFoundException | SQLException e)
            {
                System.out.println(e);
            }
        }
        if(ae.getSource()== b2)
        {
            f6.setVisible(true);
            f2.setVisible(false);
        }
        if(ae.getSource()== cl2)
        {
            f6.setVisible(false);
            f2.setVisible(true);
            utxt.setText("");
            ptxt.setText("");
            atxt.setText("");
            mtxt.setText("");
            etxt.setText("");
        }
        if(ae.getSource()== update)
        {
            try
            {
                Class.forName("com.mysql.jdbc.Driver");
                Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:33060/inventory","root","sagar");
                String sql = "update stock set name=?,quantity=?,type=?,description=? where id = ?";
                PreparedStatement pstmt = conn.prepareStatement(sql);
                int r1 = Integer.parseInt(utxt.getText());
                pstmt.setString(1,ptxt.getText());
                pstmt.setString(2,atxt.getText());
                pstmt.setString(3,mtxt.getText());
                pstmt.setString(4,etxt.getText());
                pstmt.setString(5,utxt.getText());
                JOptionPane.showMessageDialog(this,"Product "+r1+" Updated Successfully");
                pstmt.executeUpdate();
                pstmt.close();
            }
            catch(ClassNotFoundException | SQLException e)
            {
                System.out.println(e);
            }
        }
        if(ae.getSource()== b3)
        {
            f5.setVisible(true);
            f2.setVisible(false);
        }
        if(ae.getSource()== cl3)
        {
            f5.setVisible(false);
            f2.setVisible(true);
            stxt.setText("");
            sw.setText("");
        }
        if(ae.getSource()== search)
        {
            try
            {
                Class.forName("com.mysql.jdbc.Driver");
                Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:33060/inventory","root","sagar");
                String sql = "select * from stock where id = ?";
                PreparedStatement pstmt = conn.prepareStatement(sql);
                pstmt.setString(1,stxt.getText());
                ResultSet rs = pstmt.executeQuery();
                while(rs.next())
                {
                     String a = rs.getString(1); 
                     String a1 = rs.getString(2);
                     String a2 = rs.getString(3);
                     String a3 = rs.getString(4);
                     String a4 = rs.getString(5);
                     sw.setText(a + "     |    " + a1 + "      |      " + a2 + "      |      " + a3 + "      |     " + a4);
                }
                rs.close();
                pstmt.close();
            }
            catch(ClassNotFoundException | SQLException e)
            {
                System.out.println(e);
            }
        }
        if(ae.getSource()== b4)
        {
            f4.setVisible(true);
            f2.setVisible(false);
        }
        if(ae.getSource()== cl4)
        {
            f4.setVisible(false);
            f2.setVisible(true);
            idel.setText("");
        }
        if(ae.getSource()== del)
        {
            try
            {
                Class.forName("com.mysql.jdbc.Driver");
                Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:33060/inventory","root","sagar");
                String sql = "delete from stock where id = ?";
                PreparedStatement pstmt = conn.prepareStatement(sql);
                int r1 = Integer.parseInt(idel.getText());
                pstmt.setString(1,idel.getText());
                JOptionPane.showMessageDialog(this,"Product "+r1+" Deleted Successfully");
                pstmt.executeUpdate();
                pstmt.close();
            }
            catch(ClassNotFoundException | SQLException | NumberFormatException | HeadlessException e)
            {
                System.out.println(e);
            }
        }
    }
    public static void main(String[]args)
    {
        new inventory();
    }
}