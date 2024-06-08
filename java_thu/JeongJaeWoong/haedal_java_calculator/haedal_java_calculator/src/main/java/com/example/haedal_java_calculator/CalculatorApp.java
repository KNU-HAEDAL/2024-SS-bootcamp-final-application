package com.example.haedal_java_calculator;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;

import java.io.IOException;

public class CalculatorApp extends Application {
    @Override
    @SuppressWarnings("deprecation")
    public void start(Stage primaryStage) {
        try {
            Parent root = FXMLLoader.load(getClass().getResource("com/example/haedal_java_calculator/hello-view.fxml"));
            primaryStage.setTitle("Calculator");
            //gui 크기 설정
            primaryStage.setScene(new Scene(root, 300, 400));
            primaryStage.show();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }



    public static void main(String[] args) {
        //launch() : JavaFX 시작.
        launch(args);
    }
}