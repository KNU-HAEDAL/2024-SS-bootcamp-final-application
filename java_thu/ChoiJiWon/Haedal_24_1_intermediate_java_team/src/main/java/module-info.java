module com.example.calculator_hdal {
    requires javafx.controls;
    requires javafx.fxml;


    opens com.example.calculator_hdal to javafx.fxml;
    exports com.example.calculator_hdal;
}