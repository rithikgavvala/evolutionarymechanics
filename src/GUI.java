import javafx.application.Application;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.layout.HBox;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;

import java.io.IOException;
import java.io.PrintWriter;
import java.nio.file.Paths;


public class GUI extends Application {
    private TextField window_width;
    private TextField window_height;
    private TextField amount_of_Bacteria;
    private TextField cell_radius;
    private TextField growth_rate;

    public void start(Stage primaryStage) throws Exception {
        window_width = new TextField("test");
        window_height =  new TextField();
        amount_of_Bacteria = new TextField();
        cell_radius =  new TextField("test");
        growth_rate = new TextField();
        HBox hbox1 = new HBox(new Label("Window Width: "), window_width);
        HBox hbox2 = new HBox(new Label("Window Height: "), window_height);
        HBox hbox3 = new HBox(new Label("Number of Bacteria: "), amount_of_Bacteria);
        HBox hBox4 = new HBox(new Label("Cell_Radius: "), cell_radius);
        HBox hbox5 = new HBox(new Label("Growth Rate: "), growth_rate);
        Button run_sim = new Button("Run Simulation: ");
        run_sim.setAlignment(Pos.CENTER);
        VBox vbox = new VBox(hbox1, hbox2, hbox3, hBox4, hbox5, run_sim);


        run_sim.setOnAction(e -> {
            sim();
        });

        Scene scene = new Scene(vbox, 500,500);
        primaryStage.setScene(scene);
        primaryStage.setTitle("Binary Converter");
        primaryStage.setResizable(false);
        primaryStage.show();


    }

    private void sim(){
        try{
            String execPath = Paths.get(".").toAbsolutePath().normalize().toString();
            PrintWriter write = new PrintWriter(execPath + "\\main\\parameters.txt");
            write.println(window_width.getText());
            write.println(window_height.getText());
            write.println(amount_of_Bacteria.getText());
            write.println(cell_radius.getText());
            write.println(growth_rate.getText());
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

