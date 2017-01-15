package com.pk.server;

import javax.swing.*;

public class ResultDialog extends JDialog {
    public ResultDialog(JFrame parent, String message) {
        super(parent, "Nice Shot !");
        System.out.println("creating the window..");
        // set the position of the window
        // Create a message
        JPanel messagePane = new JPanel();
        messagePane.add(new JLabel(message));

        // get content pane, which is usually the
        // Container of all the dialog's components.

        Box box = new Box(BoxLayout.Y_AXIS);

        box.add(Box.createVerticalGlue());
        box.add(messagePane);
        box.add(Box.createVerticalGlue());

        getContentPane().add(box);

//        // Create a button
//        JPanel buttonPane = new JPanel();
//        JButton button = new JButton("PK");
//        buttonPane.add(button);
//        // set action listener on the butto
//        button.addActionListener(new MyActionListener());
//        getContentPane().add(buttonPane, BorderLayout.PAGE_END);
        setDefaultCloseOperation(DISPOSE_ON_CLOSE);
        pack();
        setVisible(true);
    }
}
