const api = {
	projects: () => fetch(`/projects`).then(r => r.json()),
	createProject: (name) => fetch(`/projects`, {
		method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ name })
	}).then(r => r.json()),
	issues: (projectId) => fetch(`/projects/${projectId}/issues`).then(r => r.json()),
	createIssue: (projectId, payload) => fetch(`/projects/${projectId}/issues`, {
		method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(payload)
	}).then(r => r.json()),
	updateIssue: (issueId, payload) => fetch(`/issues/${issueId}`, {
		method: 'PATCH', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(payload)
	}).then(r => r.json()),
};

const els = {
	projectSelect: document.getElementById('projectSelect'),
	refreshProjects: document.getElementById('refreshProjects'),
	createProjectForm: document.getElementById('createProjectForm'),
	projectName: document.getElementById('projectName'),
	refreshIssues: document.getElementById('refreshIssues'),
	issuesTableBody: document.querySelector('#issuesTable tbody'),
	createIssueForm: document.getElementById('createIssueForm'),
	issueTitle: document.getElementById('issueTitle'),
	issueDesc: document.getElementById('issueDesc'),
	issueSeverity: document.getElementById('issueSeverity'),
	messages: document.getElementById('messages'),
};

function setMessage(msg, kind = 'info') {
	els.messages.innerHTML = `<div class="msg ${kind}">${msg}</div>`;
}

async function loadProjects(selectFirst = true) {
	try {
		const projects = await api.projects();
		els.projectSelect.innerHTML = '';
		for (const p of projects) {
			const opt = document.createElement('option');
			opt.value = p.id;
			opt.textContent = `${p.id} - ${p.name}`;
			els.projectSelect.appendChild(opt);
		}
		if (selectFirst && projects.length) {
			els.projectSelect.value = projects[0].id;
		}
		setMessage(`Loaded ${projects.length} project(s).`);
	} catch (e) {
		setMessage(`Failed to load projects: ${e}`, 'error');
	}
}

async function loadIssues() {
	const projectId = els.projectSelect.value;
	if (!projectId) { setMessage('Select a project first', 'warn'); return; }
	try {
		const issues = await api.issues(projectId);
		els.issuesTableBody.innerHTML = '';
		for (const it of issues) {
			const tr = document.createElement('tr');
			tr.innerHTML = `
				<td>${it.id}</td>
				<td>${it.title}</td>
				<td>${it.severity}</td>
				<td>
					<select data-issue-id="${it.id}" class="statusSelect">
						${['New','In Progress','Resolved','Closed'].map(s => `<option ${s===it.status?'selected':''}>${s}</option>`).join('')}
					</select>
				</td>
				<td><button data-issue-id="${it.id}" class="btnUpdate">Update</button></td>
			`;
			els.issuesTableBody.appendChild(tr);
		}
		setMessage(`Loaded ${issues.length} issue(s).`);
	} catch (e) {
		setMessage(`Failed to load issues: ${e}`, 'error');
	}
}

async function onCreateProject(e) {
	e.preventDefault();
	const name = els.projectName.value.trim();
	if (!name) return;
	await api.createProject(name);
	els.projectName.value = '';
	await loadProjects(false);
	setMessage('Project created.');
}

async function onCreateIssue(e) {
	e.preventDefault();
	const projectId = els.projectSelect.value;
	if (!projectId) { setMessage('Select a project first', 'warn'); return; }
	const payload = {
		title: els.tissueTitle?.value || els.issueTitle.value,
		description: els.tissueDesc?.value || els.issueDesc.value,
		severity: els.tissueSeverity?.value || els.issueSeverity.value,
	};
	await api.createIssue(projectId, payload);
	els.issueTitle.value = '';
	els.issueDesc.value = '';
	await loadIssues();
	setMessage('Issue created.');
}

async function onTableClick(e) {
	const btn = e.target.closest('.btnUpdate');
	if (!btn) return;
	const id = btn.getAttribute('data-issue-id');
	const sel = btn.closest('tr').querySelector('.statusSelect');
	const status = sel.value;
	const updated = await api.updateIssue(id, { status });
	if (updated.detail) {
		setMessage(updated.detail, 'error');
	} else {
		setMessage('Issue updated.');
	}
}

document.addEventListener('DOMContentLoaded', async () => {
	els.createProjectForm.addEventListener('submit', onCreateProject);
	els.createIssueForm.addEventListener('submit', onCreateIssue);
	els.refreshProjects.addEventListener('click', () => loadProjects(false));
	els.refreshIssues.addEventListener('click', loadIssues);
	els.issuesTableBody.addEventListener('click', onTableClick);

	await loadProjects(true);
	await loadIssues();
});

