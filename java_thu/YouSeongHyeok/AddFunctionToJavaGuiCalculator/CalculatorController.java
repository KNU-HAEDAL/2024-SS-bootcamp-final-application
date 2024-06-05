package com.example.calculator;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Label;
import java.lang.Math;

public class CalculatorController {

    @FXML
    private Label displayLabel;

    private String currentInput = "";
    private double firstOperand = 0;
    private String operator = "";

    @FXML
    private void handleButtonClick(ActionEvent event) {
        String value = ((javafx.scene.control.Button) event.getSource()).getText();
        currentInput += value;
        displayLabel.setText(currentInput);
    }

    @FXML
    private void handleOperatorClick(ActionEvent event) {
        String value = ((javafx.scene.control.Button) event.getSource()).getText();
        if (!currentInput.isEmpty()) {
            firstOperand = Double.parseDouble(currentInput);
            operator = value;
            currentInput = "";
            displayLabel.setText("");
        }
    }

    @FXML
    private void handleEqualsClick(ActionEvent event) {
        if (!currentInput.isEmpty()) {
            double secondOperand = Double.parseDouble(currentInput);
            double result = calculate(firstOperand, secondOperand, operator);
            displayLabel.setText(Double.toString(result));
            currentInput = "";
        }
    }

    @FXML
    private void handleSquareRoot(ActionEvent event) {
        if (!currentInput.isEmpty()) {
            double operand = Double.parseDouble(currentInput);
            double result = Math.sqrt(operand);
            displayLabel.setText(Double.toString(result));
            currentInput = "";
        }
    }

    @FXML
    private void handleLogarithm(ActionEvent event) {
        if (!currentInput.isEmpty()) {
            double operand = Double.parseDouble(currentInput);
            double result = Math.log10(operand);
            displayLabel.setText(Double.toString(result));
            currentInput = "";
        }
    }

    private double calculate(double firstOperand, double secondOperand, String operator) {
        switch (operator) {
            case "+":
                return firstOperand + secondOperand;
            case "-":
                return firstOperand - secondOperand;
            case "*":
                return firstOperand * secondOperand;
            case "/":
                if (secondOperand != 0) {
                    return firstOperand / secondOperand;
                } else {
                    return Double.NaN;
                }
            default:
                return 0;
        }
    }
}