"use client";

import { useState } from "react";
import api from "@/lib/api";
import PredictionCard from "@/components/PredictionCard";

const defaultPayload = `{
  "features": {
    "idle_mean": 0.0,
    "fin_flag_count": 0,
    "bwd_iat_std": 910185.2072,
    "avg_bwd_segment_size": 241.0,
    "bwd_iat_max": 1576678.0,
    "packet_length_mean": 123.0,
    "fwd_iat_max": 309.0,
    "average_packet_size": 140.5714286,
    "bwd_packet_length_mean": 241.0,
    "ack_flag_count": 0,
    "cwe_flag_count": 0,
    "flow_duration": 1577064,
    "active_max": 0.0,
    "bwd_packet_length_std": 482.0,
    "fwd_urg_flags": 0,
    "fwd_packet_length_max": 20,
    "fwd_packet_length_mean": 6.666666667,
    "bwd_iat_min": 35.0,
    "idle_min": 0.0,
    "fwd_iat_mean": 174.0,
    "act_data_pkt_fwd": 1,
    "flow_iat_mean": 262844.0,
    "fwd_psh_flags": 0,
    "flow_iat_min": 3.0,
    "flow_bytes_per_s": 623.9442407,
    "fwd_packet_length_min": 0,
    "total_length_of_bwd_packets": 964.0,
    "bwd_iat_mean": 525686.6667,
    "fwd_iat_min": 39.0,
    "bwd_psh_flags": 0,
    "bwd_packets_per_s": 2.536358702,
    "urg_flag_count": 0,
    "flow_packets_per_s": 4.438627728,
    "active_std": 0.0,
    "ece_flag_count": 1,
    "down_per_up_ratio": 1,
    "idle_std": 0.0,
    "active_mean": 0.0,
    "min_packet_length": 0,
    "max_packet_length": 964,
    "fwd_packets_per_s": 1.902269026,
    "flow_iat_std": 643644.5916,
    "fwd_iat_std": 190.9188309,
    "total_length_of_fwd_packets": 20,
    "fwd_packet_length_std": 11.54700538,
    "total_backward_packets": 4,
    "min_seg_size_forward": 20,
    "bwd_packet_length_min": 0,
    "bwd_urg_flags": 0,
    "psh_flag_count": 1,
    "idle_max": 0.0,
    "init_win_bytes_backward": 211,
    "flow_iat_max": 1576678.0,
    "init_win_bytes_forward": 8192,
    "avg_fwd_segment_size": 6.666666667,
    "total_fwd_packets": 3,
    "syn_flag_count": 0,
    "active_min": 0.0,
    "packet_length_std": 339.8873763,
    "bwd_packet_length_max": 964,
    "rst_flag_count": 1,
    "packet_length_variance": 115523.4286
  }
}`;

type PredictionResult = {
  attack_type: string;
  confidence: number;
  recommended_action: string;
  binary_latency_ms: number;
  multiclass_latency_ms: number;
  total_latency_ms: number;
};

export default function PredictPage() {
  const [payload, setPayload] = useState(defaultPayload);
  const [result, setResult] = useState<PredictionResult | null>(null);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const handlePredict = async () => {
    try {
      setLoading(true);
      setError("");
      const parsed = JSON.parse(payload);
      const response = await api.post("/predict", parsed);
      setResult(response.data);
    } catch (err) {
      setError("Prediction failed. Check JSON format or backend connection.");
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className="min-h-screen bg-gray-50 p-8">
      <div className="mx-auto max-w-[1400px]">
        <h1 className="mb-2 text-4xl font-bold text-gray-900">Manual Prediction</h1>
        <p className="mb-8 text-gray-600">
          Paste a flow feature payload and test intrusion prediction
        </p>

        <div className="mb-4 flex gap-4">
          <a
            href="/"
            className="rounded-xl border border-black px-5 py-3 text-black"
          >
            Dashboard
          </a>
          <a
            href="/logs"
            className="rounded-xl border border-black px-5 py-3 text-black"
          >
            Logs
          </a>
        </div>

        <div className="grid grid-cols-1 gap-6 xl:grid-cols-2">
          <div className="rounded-2xl border border-gray-200 bg-white p-6 shadow-sm">
            <h2 className="mb-4 text-xl font-bold text-gray-900">Input JSON</h2>

            <textarea
              value={payload}
              onChange={(e) => setPayload(e.target.value)}
              className="h-[650px] w-full rounded-xl border border-gray-300 bg-gray-50 p-4 font-mono text-sm text-gray-900 outline-none"
              spellCheck={false}
            />

            <button
              onClick={handlePredict}
              disabled={loading}
              className="mt-4 rounded-xl bg-black px-5 py-3 text-white disabled:opacity-60"
            >
              {loading ? "Running..." : "Run Prediction"}
            </button>

            {error && <p className="mt-3 text-red-600">{error}</p>}
          </div>

          <div className="rounded-2xl border border-gray-200 bg-white p-6 shadow-sm">
            {!result ? (
              <>
                <h2 className="mb-4 text-xl font-bold text-gray-900">Prediction Result</h2>
                <div className="flex h-[650px] items-center justify-center rounded-xl border border-dashed border-gray-300 bg-gray-50">
                  <div className="text-center">
                    <p className="text-lg font-semibold text-gray-700">
                      No prediction yet
                    </p>
                    <p className="mt-2 text-sm text-gray-500">
                      Run the payload to view attack type, confidence, decision, and latency.
                    </p>
                  </div>
                </div>
              </>
            ) : (
              <PredictionCard result={result} />
            )}
          </div>
        </div>
      </div>
    </main>
  );
}