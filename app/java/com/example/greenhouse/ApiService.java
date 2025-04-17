package com.example.greenhouse;

import retrofit2.Call;
import retrofit2.http.GET;
import retrofit2.http.POST;
import retrofit2.http.Path;

public interface ApiService {
    @GET("/sensor")
    Call<SensorData> getSensorData();

    @POST("/control/{command}")
    Call<Void> sendCommand(@Path("command") String command);
}