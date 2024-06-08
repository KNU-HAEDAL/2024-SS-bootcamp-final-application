package com.example.demo;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;

import java.io.IOException;

public class CalculatorApp extends Application {

    //start ->  메서드는 Application 클래스의 추상 메서드로,
    //JavaFX 애플리케이션의 진입점 역할.
    //애플리케이션이 시작될 때 호출되며, 애플리케이션의 초기 설정, UI 구성 등을 담당
    @Override
    @SuppressWarnings("deprecation")
    public void start(Stage primaryStage) {
        try {
            Parent root = FXMLLoader.load(getClass().getResource("/com/example/demo/hello-view.fxml"));
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
