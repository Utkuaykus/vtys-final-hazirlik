// Data Versioning & Auto Reset for new 400 questions dataset
const DATA_VERSION = 'v2_400q_clean';
if (localStorage.getItem('vtys_data_version') !== DATA_VERSION) {
    localStorage.removeItem('vtys_completed');
    localStorage.setItem('vtys_data_version', DATA_VERSION);
}

// State
let currentExam = null;
let currentAnswers = {};
let timerInterval = null;
let timerSeconds = 0;
let completedExams = JSON.parse(localStorage.getItem('vtys_completed') || '{}');

// DOM refs
const sections = {
    home: document.getElementById('homeSection'),
    topics: document.getElementById('topicsSection'),
    exams: document.getElementById('examsSection'),
    examView: document.getElementById('examView'),
    results: document.getElementById('resultsView')
};

// ============ Navigation ============
function switchTab(tab) {
    document.querySelectorAll('.nav-btn').forEach(b => b.classList.remove('active'));
    const navBtn = document.querySelector(`[data-tab="${tab}"]`);
    if (navBtn) navBtn.classList.add('active');

    Object.values(sections).forEach(s => s.classList.add('hidden'));

    if (tab === 'home') sections.home.classList.remove('hidden');
    else if (tab === 'topics') { sections.topics.classList.remove('hidden'); renderTopicsNav(); }
    else if (tab === 'exams') { sections.exams.classList.remove('hidden'); renderExamsGrid(); }
}

document.querySelectorAll('.nav-btn').forEach(btn => {
    btn.addEventListener('click', () => switchTab(btn.dataset.tab));
});

// =============================
// Konu Analiz Haritası & Sınıflandırıcı
// =============================
const TOPIC_MAP = {
    'Temel SQL & Sorgular': 'sql-temel',
    'JOIN & Alt Sorgular': 'sql-joins-subqueries',
    'Stored Procedure': 'stored-procedure',
    'Kullanıcı Tanımlı Fonksiyonlar': 'sql-functions',
    'İlişkisel Cebir': 'iliskisel-cebir',
    'İlişkisel Model & Bütünlük': 'iliskisel-model',
    'DDL, Kısıtlar & İndeksler': 'sql-ddl',
    'Trigger (Tetikleyiciler)': 'trigger',
    'ER Modelleme & Tasarım': 'er-modelleme',
    'T-SQL Programlama': 't-sql',
    'PL/SQL Programlama': 'plsql',
    'Cursor (İmleçler)': 'cursor',
    'Normalizasyon': 'normalizasyon',
    'İşlem Yönetimi & Eşzamanlılık': 'transaction',
    'VTYS Mimarisi & Temel Kavramlar': 'vtys-mimari-temel'
};

function getQuestionTopic(q) {
    const text = ((q.q || '') + ' ' + (q.e || '')).toLowerCase();

    if (text.includes('trigger') || text.includes('tetikleyici') || text.includes('inserted') || text.includes('deleted tab')) return 'Trigger (Tetikleyiciler)';
    if (text.includes('cursor') || text.includes('imleç') || text.includes('fetch') || text.includes('deallocate') || text.includes('@@fetch_status')) return 'Cursor (İmleçler)';
    if (text.includes('procedure') || text.includes('saklı yordam') || text.includes('create proc') || text.includes('sp_')) return 'Stored Procedure';
    if (text.includes('fonksiyon') || text.includes('function') || text.includes('udf') || text.includes('skaler') || text.includes('inline table')) return 'Kullanıcı Tanımlı Fonksiyonlar';
    if (text.includes('pl/sql') || text.includes('%type') || text.includes('%rowtype') || text.includes('package') || text.includes('varray') || text.includes('raise_application_error') || text.includes('no_data_found')) return 'PL/SQL Programlama';
    if (text.includes('@@rowcount') || text.includes('@@identity') || text.includes('scope_identity') || text.includes('#tablo') || text.includes('##tablo') || text.includes('while') || text.includes('case when') || text.includes('try') || text.includes('catch') || text.includes('declare @')) return 'T-SQL Programlama';
    if (text.includes('1nf') || text.includes('2nf') || text.includes('3nf') || text.includes('bcnf') || text.includes('4nf') || text.includes('5nf') || text.includes('normalizasyon') || text.includes('kısmi bağımlılık') || text.includes('geçişli bağımlılık') || text.includes('anomali') || text.includes('armstrong') || text.includes('ayrıştırma')) return 'Normalizasyon';
    if (text.includes('er model') || text.includes('zayıf varlık') || text.includes('weak entity') || text.includes('türetilen') || text.includes('türetilmiş') || text.includes('çok değerli') || text.includes('kavşak')) return 'ER Modelleme & Tasarım';
    if (text.includes('ilişkisel cebir') || text.includes('kartezyen') || text.includes('projeksiyon') || text.includes('semijoin') || text.includes('bölme') || text.includes('σ') || text.includes('π') || text.includes('⋈')) return 'İlişkisel Cebir';
    if (text.includes('süper anahtar') || text.includes('aday anahtar') || text.includes('birincil anahtar') || text.includes('varlık bütünlüğü') || text.includes('referans bütünlüğü') || text.includes('kardinalite') || text.includes('derece')) return 'İlişkisel Model & Bütünlük';
    if (text.includes('transaction') || text.includes('acid') || text.includes('commit') || text.includes('rollback') || text.includes('dirty read') || text.includes('phantom read') || text.includes('serializable') || text.includes('2pl') || text.includes('deadlock') || text.includes('kilit')) return 'İşlem Yönetimi & Eşzamanlılık';
    if (text.includes('ansi') || text.includes('sparc') || text.includes('veri bağımsızlığı') || text.includes('dosya sistemi') || text.includes('dba') || text.includes('kavramsal düzey') || text.includes('fiziksel düzey')) return 'VTYS Mimarisi & Temel Kavramlar';
    if (text.includes('create table') || text.includes('alter table') || text.includes('drop table') || text.includes('truncate') || text.includes('foreign key') || text.includes('primary key') || text.includes('check (') || text.includes('unique') || text.includes('cascade') || text.includes('index') || text.includes('indeks') || text.includes('clustered') || text.includes('view') || text.includes('grant') || text.includes('revoke')) return 'DDL, Kısıtlar & İndeksler';
    if (text.includes('join') || text.includes('alt sorgu') || text.includes('subquery') || text.includes('exists') || text.includes('> all') || text.includes('> any') || text.includes('union') || text.includes('intersect') || text.includes('except')) return 'JOIN & Alt Sorgular';

    return 'Temel SQL & Sorgular';
}

function resetAllProgress() {
    if (confirm('Tüm çözülmüş sınav sonuçları ve konu bazlı eksik analizleriniz sıfırlanacak. Onaylıyor musunuz?')) {
        localStorage.removeItem('vtys_completed');
        completedExams = {};
        renderExamsGrid();
        alert('Tüm ilerleme ve analizler sıfırlandı. Testleri sıfırdan çözebilirsiniz!');
    }
}

function goToTopicStudy(topicId) {
    switchTab('topics');
    showTopic(topicId);
}

// ============ Topics ============
function renderTopicsNav() {
    const nav = document.getElementById('topicsNav');
    if (nav.children.length === 0) {
        TOPICS.forEach((topic, i) => {
            const item = document.createElement('div');
            item.className = 'topic-nav-item';
            item.dataset.topicId = topic.id;
            const priorityClass = topic.priority === 'high' ? 'priority-high' : topic.priority === 'medium' ? 'priority-medium' : 'priority-low';
            const priorityLabel = topic.priority === 'high' ? 'YÜKSEK' : topic.priority === 'medium' ? 'ORTA' : 'DÜŞÜK';
            item.innerHTML = `
                <span class="topic-nav-icon">${topic.icon}</span>
                <span>${topic.title}</span>
                <span class="topic-nav-priority ${priorityClass}">${priorityLabel}</span>
            `;
            item.addEventListener('click', () => showTopic(topic.id));
            nav.appendChild(item);
        });
    }
    const activeItem = nav.querySelector('.topic-nav-item.active');
    if (!activeItem && TOPICS.length > 0) {
        showTopic(TOPICS[0].id);
    }
}

function showTopic(topicId) {
    const topic = TOPICS.find(t => t.id === topicId);
    if (!topic) return;

    document.querySelectorAll('.topic-nav-item').forEach(i => i.classList.remove('active'));
    const activeItem = document.querySelector(`[data-topic-id="${topicId}"]`);
    if (activeItem) activeItem.classList.add('active');

    const area = document.getElementById('topicContentArea');
    const priorityClass = topic.priority === 'high' ? 'priority-high' : topic.priority === 'medium' ? 'priority-medium' : 'priority-low';
    const priorityLabel = topic.priority === 'high' ? '🔥 YÜKSEK ÖNCELİK' : topic.priority === 'medium' ? '⭐ ORTA ÖNCELİK' : '📘 DÜŞÜK ÖNCELİK';

    area.innerHTML = `
        <div class="topic-title">
            <span class="topic-title-icon">${topic.icon}</span>
            ${topic.title}
            <span class="topic-priority-badge ${priorityClass}">${priorityLabel}</span>
        </div>
        <p class="topic-subtitle">${topic.subtitle}</p>
        ${topic.content}
    `;
    area.scrollTop = 0;
}

// ============ Exams Grid ============
function renderExamsGrid() {
    renderGlobalAnalysis();
    const grid = document.getElementById('examsGrid');
    grid.innerHTML = '';
    EXAMS.forEach(exam => {
        const completed = completedExams[exam.id];
        const card = document.createElement('div');
        card.className = 'exam-card';
        card.innerHTML = `
            <div class="exam-card-number">${exam.id}</div>
            <div class="exam-card-title">${exam.title}</div>
            <div class="exam-card-desc">${exam.desc}</div>
            <div class="exam-card-topics">
                ${exam.topics.slice(0, 5).map(t => `<span class="topic-chip">${t}</span>`).join('')}
            </div>
            <div class="exam-card-footer">
                <span class="exam-card-count">📝 ${exam.questions.length} soru</span>
                ${completed
                    ? `<span class="exam-card-status status-done">✅ Sonuç: ${completed.score}/${completed.total} (%${completed.percentage})</span>`
                    : `<span class="exam-card-status status-new">🆕 Çözülmedi</span>`
                }
            </div>
        `;
        card.addEventListener('click', () => handleExamClick(exam.id));
        grid.appendChild(card);
    });
}

function renderGlobalAnalysis() {
    const container = document.getElementById('globalAnalysisContainer');
    if (!container) return;

    const completedIds = Object.keys(completedExams);
    if (completedIds.length === 0) {
        container.innerHTML = '';
        return;
    }

    const topicStats = {};

    completedIds.forEach(examId => {
        const saved = completedExams[examId];
        const exam = EXAMS.find(e => e.id == examId);
        if (!exam || !saved.answers) return;

        exam.questions.forEach((q, qi) => {
            const topic = getQuestionTopic(q);
            if (!topicStats[topic]) topicStats[topic] = { correct: 0, total: 0 };
            topicStats[topic].total++;
            if (saved.answers[qi] !== undefined && saved.answers[qi] === q.a) {
                topicStats[topic].correct++;
            }
        });
    });

    const topicKeys = Object.keys(topicStats);
    if (topicKeys.length === 0) {
        container.innerHTML = '';
        return;
    }

    const weakTopics = [];
    const strongTopics = [];

    topicKeys.forEach(t => {
        const pct = Math.round((topicStats[t].correct / topicStats[t].total) * 100);
        if (pct < 70) weakTopics.push({ topic: t, pct, correct: topicStats[t].correct, total: topicStats[t].total });
        else strongTopics.push({ topic: t, pct, correct: topicStats[t].correct, total: topicStats[t].total });
    });

    weakTopics.sort((a, b) => a.pct - b.pct);
    strongTopics.sort((a, b) => b.pct - a.pct);

    container.innerHTML = `
        <div class="global-analysis-card">
            <div class="topic-analysis-title">
                <span>📊 Genel Eksik & Performans Analizi (${completedIds.length} Sınav Çözüldü)</span>
            </div>
            <div class="global-analysis-grid">
                <div class="analysis-box">
                    <div class="analysis-box-title" style="color: var(--error)">
                        <span>🔥 Geliştirilmesi Gereken Konular (Eksiklerin)</span>
                    </div>
                    ${weakTopics.length > 0 ? weakTopics.map(w => `
                        <div class="topic-stat-item" style="margin-bottom: 8px;">
                            <div class="topic-stat-header">
                                <span class="topic-stat-name">${w.topic}</span>
                                <span class="topic-stat-badge badge-danger">%${w.pct} (${w.correct}/${w.total})</span>
                            </div>
                            <button class="btn-study-topic" onclick="goToTopicStudy('${TOPIC_MAP[w.topic] || 'sql-temel'}')">📚 Konuyu İncele →</button>
                        </div>
                    `).join('') : '<p style="font-size:0.85rem; color:var(--text-muted)">Henüz belirgin bir eksik konu tespit edilmedi. Harika gidiyorsun! 🎉</p>'}
                </div>
                <div class="analysis-box">
                    <div class="analysis-box-title" style="color: var(--success)">
                        <span>✅ Başarılı Olduğun Güçlü Konular</span>
                    </div>
                    ${strongTopics.length > 0 ? strongTopics.map(s => `
                        <div class="topic-stat-item" style="margin-bottom: 8px;">
                            <div class="topic-stat-header">
                                <span class="topic-stat-name">${s.topic}</span>
                                <span class="topic-stat-badge badge-success">%${s.pct} (${s.correct}/${s.total})</span>
                            </div>
                        </div>
                    `).join('') : '<p style="font-size:0.85rem; color:var(--text-muted)">Daha fazla test çözerek güçlü yönlerini keşfet!</p>'}
                </div>
            </div>
        </div>
    `;
}

function handleExamClick(examId) {
    const completed = completedExams[examId];
    if (completed && completed.answers) {
        // Exam already completed and has saved answers -> show results & review mode
        openSavedResults(examId);
    } else {
        // Start fresh exam
        startExam(examId, true);
    }
}

// ============ Exam ============
function startExam(examId, forceReset = false) {
    const exam = EXAMS.find(e => e.id === examId);
    if (!exam) return;

    currentExam = exam;
    currentAnswers = {};
    timerSeconds = 0;

    Object.values(sections).forEach(s => s.classList.add('hidden'));
    sections.examView.classList.remove('hidden');

    document.getElementById('examTitle').textContent = exam.title;
    document.getElementById('examQuestionCount').textContent = `📝 ${exam.questions.length} soru`;
    document.getElementById('progressBar').style.width = '0%';
    document.getElementById('progressText').textContent = `0/${exam.questions.length}`;

    renderQuestions(exam.questions);
    startTimer();
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

function renderQuestions(questions) {
    const container = document.getElementById('questionsContainer');
    container.innerHTML = '';
    const letters = ['A', 'B', 'C', 'D', 'E'];

    questions.forEach((q, qi) => {
        const card = document.createElement('div');
        card.className = 'question-card';
        card.id = `q-${qi}`;

        let questionHTML = q.q;
        // Handle code blocks
        if (questionHTML.includes('\n')) {
            const parts = questionHTML.split('\n');
            const textPart = parts[0];
            const codePart = parts.slice(1).join('\n');
            questionHTML = `${textPart}<div class="code-block-full">${codePart}</div>`;
        }

        card.innerHTML = `
            <div class="question-number">
                <span class="q-badge">Soru ${qi + 1}</span>
            </div>
            <div class="question-text">${questionHTML}</div>
            <div class="options-list">
                ${q.o.map((opt, oi) => `
                    <div class="option-item" data-question="${qi}" data-option="${oi}">
                        <span class="option-letter">${letters[oi]}</span>
                        <span class="option-text">${opt}</span>
                    </div>
                `).join('')}
            </div>
            <div class="explanation" id="exp-${qi}">
                <strong>📖 Açıklama:</strong> ${q.e}
            </div>
        `;
        container.appendChild(card);
    });

    // Option click handlers
    container.querySelectorAll('.option-item').forEach(item => {
        item.addEventListener('click', function() {
            const qi = parseInt(this.dataset.question);
            const oi = parseInt(this.dataset.option);
            selectOption(qi, oi);
        });
    });
}

function selectOption(qi, oi) {
    currentAnswers[qi] = oi;

    // Update UI
    const card = document.getElementById(`q-${qi}`);
    card.classList.add('answered');
    card.querySelectorAll('.option-item').forEach(item => {
        item.classList.remove('selected');
        if (parseInt(item.dataset.option) === oi) {
            item.classList.add('selected');
        }
    });

    updateProgress();
}

function updateProgress() {
    const total = currentExam.questions.length;
    const answered = Object.keys(currentAnswers).length;
    const pct = (answered / total) * 100;
    document.getElementById('progressBar').style.width = `${pct}%`;
    document.getElementById('progressText').textContent = `${answered}/${total}`;
}

// ============ Timer ============
function startTimer() {
    if (timerInterval) clearInterval(timerInterval);
    timerSeconds = 0;
    timerInterval = setInterval(() => {
        timerSeconds++;
        const mins = Math.floor(timerSeconds / 60).toString().padStart(2, '0');
        const secs = (timerSeconds % 60).toString().padStart(2, '0');
        document.getElementById('examTimer').textContent = `⏱️ ${mins}:${secs}`;
    }, 1000);
}

function stopTimer() {
    if (timerInterval) clearInterval(timerInterval);
}

// ============ Submit ============
document.getElementById('btnSubmit').addEventListener('click', () => {
    const total = currentExam.questions.length;
    const answered = Object.keys(currentAnswers).length;

    if (answered < total) {
        if (!confirm(`${total - answered} soru cevaplanmadı. Yine de bitirmek istiyor musunuz?`)) return;
    }

    stopTimer();
    showResults();
});

function showResults() {
    const questions = currentExam.questions;
    let correct = 0;
    let wrong = 0;
    let unanswered = 0;

    questions.forEach((q, qi) => {
        if (currentAnswers[qi] !== undefined) {
            if (currentAnswers[qi] === q.a) correct++;
            else wrong++;
        } else {
            unanswered++;
        }
    });

    const total = questions.length;
    const score = Math.round((correct / total) * 100);

    // Save progress WITH ANSWERS in localStorage
    completedExams[currentExam.id] = {
        score: correct,
        total,
        percentage: score,
        answers: currentAnswers,
        timerSeconds: timerSeconds
    };
    localStorage.setItem('vtys_completed', JSON.stringify(completedExams));

    displayResultsView(correct, wrong, unanswered, score);
}

function openSavedResults(examId) {
    const exam = EXAMS.find(e => e.id === examId);
    const saved = completedExams[examId];
    if (!exam || !saved) return;

    currentExam = exam;
    currentAnswers = saved.answers || {};

    let correct = saved.score;
    let total = saved.total || exam.questions.length;
    let wrong = 0;
    let unanswered = 0;

    exam.questions.forEach((q, qi) => {
        const ans = currentAnswers[qi];
        if (ans !== undefined) {
            if (ans !== q.a) wrong++;
        } else {
            unanswered++;
        }
    });

    displayResultsView(correct, wrong, unanswered, saved.percentage);
    
    // Automatically render review mode when opened from saved
    const reviewContainer = document.getElementById('reviewContainer');
    reviewContainer.classList.remove('hidden');
    renderReview();
}

function displayResultsView(correct, wrong, unanswered, score) {
    // Show results section
    Object.values(sections).forEach(s => s.classList.add('hidden'));
    sections.results.classList.remove('hidden');

    // Score animation
    const scoreFill = document.getElementById('scoreFill');
    const circumference = 2 * Math.PI * 54; // 339.292
    const offset = circumference - (score / 100) * circumference;
    setTimeout(() => {
        scoreFill.style.strokeDashoffset = offset;
    }, 100);

    document.getElementById('scoreText').textContent = score;

    // Stats
    const statsDiv = document.getElementById('resultsStats');
    statsDiv.innerHTML = `
        <div class="result-stat success">
            <div class="result-stat-value">${correct}</div>
            <div class="result-stat-label">Doğru</div>
        </div>
        <div class="result-stat error">
            <div class="result-stat-value">${wrong}</div>
            <div class="result-stat-label">Yanlış</div>
        </div>
        <div class="result-stat info">
            <div class="result-stat-value">${unanswered}</div>
            <div class="result-stat-label">Boş</div>
        </div>
    `;

    renderTopicAnalysis(currentExam, currentAnswers);

    window.scrollTo({ top: 0, behavior: 'smooth' });
}

function renderTopicAnalysis(exam, answers) {
    const container = document.getElementById('topicAnalysisContainer');
    if (!container || !exam) return;

    const topicStats = {};

    exam.questions.forEach((q, qi) => {
        const topic = getQuestionTopic(q);
        if (!topicStats[topic]) {
            topicStats[topic] = { correct: 0, total: 0 };
        }
        topicStats[topic].total++;
        if (answers[qi] !== undefined && answers[qi] === q.a) {
            topicStats[topic].correct++;
        }
    });

    let html = `
        <div class="topic-analysis-title">
            <span>🎯 Konu Bazlı Başarı & Eksik Analizi</span>
        </div>
        <div class="topic-stat-list">
    `;

    Object.keys(topicStats).forEach(topic => {
        const stat = topicStats[topic];
        const pct = Math.round((stat.correct / stat.total) * 100);
        let badgeClass = 'badge-success';
        let fillClass = 'fill-success';
        let statusLabel = '✅ Başarılı';

        if (pct < 50) {
            badgeClass = 'badge-danger';
            fillClass = 'fill-danger';
            statusLabel = '🔥 Acil Çalış (Eksik)';
        } else if (pct < 75) {
            badgeClass = 'badge-warning';
            fillClass = 'fill-warning';
            statusLabel = '⚠️ Tekrar Et';
        }

        const targetTopicId = TOPIC_MAP[topic] || 'sql-temel';

        html += `
            <div class="topic-stat-item">
                <div class="topic-stat-header">
                    <span class="topic-stat-name">${topic}</span>
                    <span class="topic-stat-badge ${badgeClass}">${statusLabel}</span>
                </div>
                <div class="topic-progress-wrapper">
                    <div class="topic-bar-bg">
                        <div class="topic-bar-fill ${fillClass}" style="width: ${pct}%"></div>
                    </div>
                    <span class="topic-stat-pct">%${pct} (${stat.correct}/${stat.total})</span>
                </div>
                ${pct < 75 ? `<button class="btn-study-topic" onclick="goToTopicStudy('${targetTopicId}')">📚 Konu Anlatımını Oku →</button>` : ''}
            </div>
        `;
    });

    html += `</div>`;
    container.innerHTML = html;
}


// ============ Review ============
document.getElementById('btnReview').addEventListener('click', () => {
    const reviewContainer = document.getElementById('reviewContainer');
    reviewContainer.classList.toggle('hidden');

    if (!reviewContainer.classList.contains('hidden')) {
        renderReview();
    }
});

function renderReview() {
    const container = document.getElementById('reviewContainer');
    container.innerHTML = '';
    const letters = ['A', 'B', 'C', 'D', 'E'];
    const questions = currentExam.questions;

    questions.forEach((q, qi) => {
        const userAnswer = currentAnswers[qi];
        const isCorrect = userAnswer === q.a;
        const isAnswered = userAnswer !== undefined;

        const card = document.createElement('div');
        card.className = `question-card ${isAnswered ? (isCorrect ? 'correct' : 'incorrect') : ''}`;

        let questionHTML = q.q;
        if (questionHTML.includes('\n')) {
            const parts = questionHTML.split('\n');
            questionHTML = `${parts[0]}<div class="code-block-full">${parts.slice(1).join('\n')}</div>`;
        }

        card.innerHTML = `
            <div class="question-number">
                <span class="q-badge">Soru ${qi + 1}</span>
                ${isAnswered ? (isCorrect ? '✅ Doğru' : '❌ Yanlış') : '⬜ Boş'}
            </div>
            <div class="question-text">${questionHTML}</div>
            <div class="options-list">
                ${q.o.map((opt, oi) => {
                    let cls = '';
                    if (oi === q.a) cls = 'correct-answer';
                    else if (oi === userAnswer && oi !== q.a) cls = 'wrong-answer';
                    return `
                        <div class="option-item ${cls}">
                            <span class="option-letter">${letters[oi]}</span>
                            <span class="option-text">${opt}</span>
                        </div>
                    `;
                }).join('')}
            </div>
            <div class="explanation show">
                <strong>📖 Açıklama:</strong> ${q.e}
            </div>
        `;
        container.appendChild(card);
    });
}

// ============ Result Actions ============
document.getElementById('btnRetake').addEventListener('click', () => {
    startExam(currentExam.id, true);
});

document.getElementById('btnBackToExams').addEventListener('click', () => {
    switchTab('exams');
});

// ============ Back Button ============
document.getElementById('btnBack').addEventListener('click', () => {
    if (confirm('Sınavı bırakmak istediğinize emin misiniz? İlerlemeniz kaybolacak.')) {
        stopTimer();
        switchTab('exams');
    }
});

// ============ Init ============
renderExamsGrid();

