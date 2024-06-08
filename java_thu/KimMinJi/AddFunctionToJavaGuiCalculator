package com.example.demo;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.control.Label;

public class CalculatorController {


//JavaFX에서 @FXML은 FXML 파일로부터 UI 요소를 컨트롤러 클래스에 주입하기 위해 사용되는 어노테이션입니다.
//JavaFX에서 UI를 디자인하고 정의하는 방법 중 하나는 FXML(Flexible Markup Language)을 사용하는 것입니다. FXML은 XML 기반의 마크업 언어로, 시각적인 구성 요소를 표현하고 애플리케이션의 레이아웃을 정의할 수 있습니다. FXML 파일은 일반적으로 UI 요소의 계층 구조를 정의하고, 이벤트 핸들러와 같은 이벤트를 연결하는 등의 작업을 할 수 있습니다.
//어노테이션은 FXML 파일에서 정의한 UI 요소를 컨트롤러 클래스에서 사용할 수 있도록 연결해 줍니다. 예를 들어, FXML 파일에서 정의한 버튼이나 텍스트 필드와 같은 UI 요소를 컨트롤러 클래스에서 필드로 선언하고, 해당 필드에 @FXML 어노테이션을 붙여주면 FXML 로더가 해당 UI 요소와 연결하여 자동으로 초기화해 줍니다.

    @FXML
    private Label displayLabel;

//JavaFX의 라벨(Label) 객체는 사용자 인터페이스(UI)에서 텍스트를 표시하는 데 사용됩니다. 일반적으로 정적인 텍스트나 애플리케이션의 상태나 정보를 사용자에게 전달하는 데에 활용됩니다.
//
//라벨(Label) 객체의 주요 특징은 다음과 같습니다:
//
//텍스트 표시: 라벨은 텍스트를 표시하는 데 사용됩니다. 이를 통해 사용자에게 메시지를 전달하거나, 어떤 내용을 설명하는 데에 활용할 수 있습니다.
//
//스타일링: JavaFX에서는 CSS(Cascading Style Sheets)를 사용하여 UI 요소를 스타일링할 수 있습니다. 따라서 라벨도 CSS를 사용하여 텍스트의 폰트, 색상, 배경 등을 스타일링할 수 있습니다.
//
//이벤트 처리: 라벨은 마우스 클릭 등의 이벤트를 처리할 수 있습니다. 이를 통해 사용자의 상호작용에 대응하여 특정 동작을 수행할 수 있습니다.

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
    //ActionEvent : JavaFX에서 이벤트가 발생했을 때 전달되는 이벤트 객체
    private void handleEqualsClick(ActionEvent event) {
        if (!currentInput.isEmpty()) {
            double secondOperand = Double.parseDouble(currentInput);
            //calculate는 내가 정의한 내부 메서드
            double result = calculate(firstOperand, secondOperand, operator);
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
                    // handle division by zero
                    return Double.NaN;
                }
            case "^":
                return Math.pow(firstOperand, secondOperand);

            default:
                return 0;
        }
    }
}
