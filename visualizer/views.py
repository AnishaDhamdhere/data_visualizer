# analysis/views.py

import matplotlib
matplotlib.use('Agg')  # Use a non-interactive backend

from django.shortcuts import render, redirect
from .forms import UploadFileForm
from .models import UploadedFile
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.save()
            return redirect('visualizer:results', pk=uploaded_file.pk)
    else:
        form = UploadFileForm()
    return render(request, 'visualizer/upload.html', {'form': form})

def file_analysis(request, pk):
    uploaded_file = UploadedFile.objects.get(pk=pk)
    file_path = uploaded_file.file.path
    df = pd.read_csv(file_path)

    # Basic data analysis
    head = df.head().to_html()
    summary_stats = df.describe().to_html()
    missing_values = df.isnull().sum().to_frame(name='Missing Values').to_html()  # Convert Series to DataFrame

    sns.set(style="whitegrid")
    plots = []

    for column in df.select_dtypes(include=[np.number]).columns:
        plt.figure()
        sns.histplot(df[column].dropna(), kde=True)
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        plt.close()
        buf.seek(0)
        image_png = buf.getvalue()
        buf.close()
        plot = base64.b64encode(image_png).decode('utf-8')
        plots.append(plot)

    return render(request, 'visualizer/results.html', {
        'head': head,
        'summary_stats': summary_stats,
        'missing_values': missing_values,
        'plots': plots,
    })
