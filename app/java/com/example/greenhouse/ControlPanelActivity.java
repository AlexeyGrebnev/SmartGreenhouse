package com.example.greenhouse;

import android.os.Bundle;
import android.widget.Button;
import android.widget.Toast;
import androidx.appcompat.app.AppCompatActivity;
import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class ControlPanelActivity extends AppCompatActivity {
    private Button lightButton, fanButton, waterButton;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_control);

        lightButton = findViewById(R.id.btn_light);
        fanButton = findViewById(R.id.btn_fan);
        waterButton = findViewById(R.id.btn_water);

        ApiService api = NetworkService.getInstance().getApi();

        lightButton.setOnClickListener(v -> sendCommand(api, "light_on"));
        fanButton.setOnClickListener(v -> sendCommand(api, "fan_on"));
        waterButton.setOnClickListener(v -> sendCommand(api, "water_on"));
    }

    private void sendCommand(ApiService api, String command) {
        api.sendCommand(command).enqueue(new Callback<Void>() {
            @Override
            public void onResponse(Call<Void> call, Response<Void> response) {
                Toast.makeText(ControlPanelActivity.this, "Команда отправлена", Toast.LENGTH_SHORT).show();
            }

            @Override
            public void onFailure(Call<Void> call, Throwable t) {
                Toast.makeText(ControlPanelActivity.this, "Ошибка отправки", Toast.LENGTH_SHORT).show();
            }
        });
    }
}