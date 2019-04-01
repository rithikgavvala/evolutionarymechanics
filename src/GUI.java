import javafx.application.Application;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.layout.HBox;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;

import java.io.File;
import java.io.IOException;
import java.io.PrintWriter;
import java.nio.file.Paths;
import java.util.Scanner;


public class GUI extends Application {
    private TextField window_width;
    private TextField window_height;
    private TextField amount_of_Bacteria;
    private TextField cell_radius;
    private TextField growth_rate;
    private TextField num_tracers;
    private ToggleGroup group;
    private  RadioButton button1;
    private  RadioButton button2;
    private ToggleGroup group2;
    private  RadioButton button3;
    private  RadioButton button4;
    private  Scanner Path;
    private String dataPath;


    public void start(Stage primaryStage) throws Exception {
        String execPath = Paths.get(".").toAbsolutePath().normalize().toString();
        Scanner scanner = new Scanner(new File(execPath + "\\main\\parameters.txt"));
        //Scanner path = new Scanner(new File(execPath + "\\main\\path.txt"));
        //dataPath = path.nextLine() +"\\data\\parameters.txt";
        //Scanner scanner = new Scanner(new File(dataPath));
        scanner.useDelimiter("\n");

        window_width = new TextField(scanner.nextLine());
        window_height =  new TextField(scanner.nextLine());
        amount_of_Bacteria = new TextField(scanner.nextLine());
        cell_radius =  new TextField(scanner.nextLine());
        growth_rate = new TextField(scanner.nextLine());
        scanner.nextLine();
        scanner.nextLine();
        num_tracers = new TextField(scanner.nextLine());


        group = new ToggleGroup();
        button1 = new RadioButton("Yes");
        button1.setToggleGroup(group);
        button1.setSelected(true);
        button2 = new RadioButton("No");
        button2.setToggleGroup(group);

        group2 = new ToggleGroup();
        button3 = new RadioButton("Yes");
        button3.setToggleGroup(group2);
        button3.setSelected(true);
        button4 = new RadioButton("No");
        button4.setToggleGroup(group2);


        HBox hbox1 = new HBox(new Label("Window Width: "), window_width);
        HBox hbox2 = new HBox(new Label("Window Height: "), window_height);
        HBox hbox3 = new HBox(new Label("Number of Bacteria: "), amount_of_Bacteria);
        HBox hBox4 = new HBox(new Label("Cell_Radius: "), cell_radius);
        HBox hbox5 = new HBox(new Label("Growth Rate: "), growth_rate);
        HBox hbox8 = new HBox(new Label("Amount of Tracers: "), num_tracers);
        HBox hbox6 = new HBox(new Label("Turn Killing on: "), button1, button2);
        HBox hbox7 = new HBox(new Label("Turn Dividing on: "), button3, button4);
        Button run_sim = new Button("Run Simulation: ");
        run_sim.setAlignment(Pos.CENTER);
        VBox vbox = new VBox(hbox1, hbox2, hbox3, hBox4, hbox5, hbox8, hbox6, hbox7, run_sim);


        run_sim.setOnAction(e -> {
            sim();
        });
        //path.close();
        Scene scene = new Scene(vbox, 500,500);
        primaryStage.setScene(scene);
        primaryStage.setTitle("Simulation Parameters");
        primaryStage.setResizable(false);
        primaryStage.show();


    }

    private void sim(){
        try{
            String execPath = Paths.get(".").toAbsolutePath().normalize().toString();
            PrintWriter write = new PrintWriter(execPath + "\\main\\parameters.txt");

            //PrintWriter write = new PrintWriter(dataPath);
            write.println(window_width.getText());
            write.println(window_height.getText());
            write.println(amount_of_Bacteria.getText());
            write.println(cell_radius.getText());
            write.println(growth_rate.getText());
            if(button1.isSelected()){
                write.println("1");
            } else{
                write.println("0");
            }
            if(button3.isSelected()){
                write.println("1");
            } else{
                write.println("0");
            }
            write.println(num_tracers.getText());
            write.close();

            Runtime runTime = Runtime.getRuntime();
            System.out.println(execPath);
            Process process = runTime.exec(execPath +  "\\main\\application.windows32\\main.exe");

        } catch (IOException e){
            System.out.println("it failed");
        }

    }
    public static void main(String[] args){launch(args);}

    }

