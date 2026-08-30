import React, { useCallback, useEffect, useMemo, useRef, useState } from "react"
import ReactDOM from "react-dom/client"
import * as Slider from "@radix-ui/react-slider"
import { motion, useReducedMotion } from "motion/react"
import { Puck } from "@puckeditor/core"
import { GridLayout, useContainerWidth } from "react-grid-layout"
import "@puckeditor/core/puck.css"
import "react-grid-layout/css/styles.css"
import "./styles.css"
import "./auto.css"

const LEVELS = ["xsmall", "small", "medium", "large", "xlarge"]
const LABELS = { xsmall: "매우 작게", small: "작게", medium: "보통", large: "크게", xlarge: "매우 크게" }
const INITIAL_CARDS = [
  { id: "pdf-result-preview", title: "PDF 도면 기호", description: "도면의 문·창문·벽·기호를 확인하는 결과물", accent: "#00a86b", secondary: "#f1a35b", surface: "#eefaf5", textColor: "#10251f", paletteMode: "twoTone", imageUrl: "", imageName: "", fontSize: "medium" },
  { id: "hospital-web-result-preview", title: "동네 병원 웹", description: "의료진·예약·병원 정보를 제공하는 웹 결과물", accent: "#356cf6", secondary: "#f0a55f", surface: "#f1f5ff", textColor: "#14213d", paletteMode: "twoTone", imageUrl: "", imageName: "", fontSize: "medium" },
  { id: "research-summary", title: "자료 조사 요약", description: "선택한 프로젝트에 필요한 근거와 참고 자료", accent: "#f05a28", secondary: "#2e8b78", surface: "#fff4ef", textColor: "#35160c", paletteMode: "single", imageUrl: "", imageName: "", fontSize: "medium" },
]
const INITIAL_LAYOUTS = {
  desktop: [
    { i: "pdf-result-preview", x: 0, y: 0, w: 6, h: 4, minW: 3, maxW: 12, minH: 2, maxH: 8 },
    { i: "hospital-web-result-preview", x: 6, y: 0, w: 6, h: 4, minW: 3, maxW: 12, minH: 2, maxH: 8 },
    { i: "research-summary", x: 0, y: 4, w: 12, h: 3, minW: 3, maxW: 12, minH: 2, maxH: 8 },
  ],
  mobile: [
    { i: "pdf-result-preview", x: 0, y: 0, w: 4, h: 4, minW: 2, maxW: 4, minH: 2, maxH: 8 },
    { i: "hospital-web-result-preview", x: 0, y: 4, w: 4, h: 4, minW: 2, maxW: 4, minH: 2, maxH: 8 },
    { i: "research-summary", x: 0, y: 8, w: 4, h: 3, minW: 2, maxW: 4, minH: 2, maxH: 8 },
  ],
}
const clone = (value) => JSON.parse(JSON.stringify(value))
const initialSnapshot = () => ({ cards: clone(INITIAL_CARDS), layouts: clone(INITIAL_LAYOUTS) })
const fontWeight = { xsmall: 0, small: 1, medium: 2, large: 3, xlarge: 4 }
function hexToHsl(hex) {
  const value = hex.replace("#", "")
  const r = parseInt(value.slice(0, 2), 16) / 255, g = parseInt(value.slice(2, 4), 16) / 255, b = parseInt(value.slice(4, 6), 16) / 255
  const max = Math.max(r, g, b), min = Math.min(r, g, b), delta = max - min
  let h = 0
  if (delta) h = max === r ? ((g - b) / delta) % 6 : max === g ? (b - r) / delta + 2 : (r - g) / delta + 4
  h = Math.round(h * 60); if (h < 0) h += 360
  const l = (max + min) / 2
  const s = delta ? delta / (1 - Math.abs(2 * l - 1)) : 0
  return { h, s: Math.round(s * 100), l: Math.round(l * 100) }
}
function hslToHex(h, s, l) {
  s /= 100; l /= 100
  const c = (1 - Math.abs(2 * l - 1)) * s, x = c * (1 - Math.abs((h / 60) % 2 - 1)), m = l - c / 2
  let rgb = [0, 0, 0]
  if (h < 60) rgb = [c, x, 0]; else if (h < 120) rgb = [x, c, 0]; else if (h < 180) rgb = [0, c, x]; else if (h < 240) rgb = [0, x, c]; else if (h < 300) rgb = [x, 0, c]; else rgb = [c, 0, x]
  return `#${rgb.map((channel) => Math.round((channel + m) * 255).toString(16).padStart(2, "0")).join("")}`
}
function createPalette(accent) {
  const { h, s } = hexToHsl(accent)
  return { accent, secondary: hslToHex((h + 38) % 360, Math.max(32, Math.min(62, s - 12)), 66), surface: hslToHex(h, Math.max(18, Math.min(38, s - 28)), 95), textColor: hslToHex(h, Math.max(22, Math.min(42, s - 24)), 17), paletteMode: "twoTone" }
}
function createAutoLayouts(cards) {
  const heightFor = (card, mobile = false) => {
    const score = card.title.length * 1.4 + card.description.length + fontWeight[card.fontSize] * 10
    return Math.min(8, Math.max(3, Math.ceil(score / (mobile ? 32 : 48)) + 2))
  }
  const desktopHeights = cards.map((card) => heightFor(card))
  const firstRowHeight = Math.max(...desktopHeights.slice(0, 2), 0)
  let mobileY = 0
  return {
    desktop: cards.map((card, index) => ({ i: card.id, x: index < 2 ? index * 6 : 0, y: index < 2 ? 0 : firstRowHeight, w: index < 2 ? 6 : 12, h: desktopHeights[index], minW: 3, maxW: 12, minH: 2, maxH: 8 })),
    mobile: cards.map((card) => {
      const height = heightFor(card, true)
      const layout = { i: card.id, x: 0, y: mobileY, w: 4, h: height, minW: 2, maxW: 4, minH: 2, maxH: 8 }
      mobileY += height
      return layout
    }),
  }
}

function FiveStepField({ value = "medium", onChange, readOnly, field }) {
  const index = Math.max(0, LEVELS.indexOf(value))
  return <div className="level-field"><div className="level-field__value"><span>{field.label}</span><strong>{LABELS[value]}</strong></div><Slider.Root className="level-slider" min={0} max={4} step={1} value={[index]} disabled={readOnly} onValueChange={([next]) => onChange(LEVELS[next])}><Slider.Track className="level-slider__track"><Slider.Range className="level-slider__range" /></Slider.Track><Slider.Thumb className="level-slider__thumb" aria-label={`${field.label} 5단계`} /></Slider.Root></div>
}
function ColorField({ value = "#00a86b", onChange, readOnly, field }) {
  return <label className="color-field"><span>{field.label}</span><span className="color-field__control"><input type="color" value={value} disabled={readOnly} onChange={(event) => onChange(event.target.value)} /><code>{value}</code></span></label>
}
function ResultCard({ title, description, accent, secondary = accent, surface = "#ffffff", textColor = "#10251f", paletteMode = "single", imageUrl = "", imageName = "", fontSize = "medium", textFit = "default", overflow = false, selected = false, onSelect }) {
  const reduceMotion = useReducedMotion()
  return <motion.article layout data-text-fit={textFit} data-palette-mode={paletteMode} className={`result-card${selected ? " is-selected" : ""}${imageUrl ? " has-image" : ""}`} style={{ "--card-accent": accent, "--card-secondary": secondary, "--card-surface": surface, "--card-text": textColor }} transition={reduceMotion ? { duration: 0 } : { type: "spring", stiffness: 360, damping: 32 }} onClick={onSelect}>
    <div className="result-card__handle" aria-label="카드 이동 손잡이">⋮⋮</div>{imageUrl ? <div className="result-card__image"><img src={imageUrl} alt={imageName || `${title} 이미지`} /></div> : null}<div className="result-card__content"><div className="result-card__eyebrow">프로젝트 결과</div><h2 data-font-size={fontSize}>{title}</h2><p>{description}</p><div className="result-card__footer"><span>확인 가능</span><button type="button">열기</button></div></div>{overflow ? <div className="overflow-warning" role="status">내용이 넘칩니다. 카드 높이를 늘려주세요.</div> : null}
  </motion.article>
}
const puckConfig = { categories: { results: { title: "검증된 결과 모듈" } }, components: { ResultCard: { label: "프로젝트 결과 카드", fields: { title: { type: "text", label: "제목" }, description: { type: "textarea", label: "설명" }, accent: { type: "custom", label: "대표 색상", render: ColorField }, fontSize: { type: "custom", label: "글씨 크기", render: FiveStepField } }, defaultProps: { title: "새 프로젝트 결과", description: "사용자가 확인할 결과물입니다.", accent: "#00a86b", fontSize: "medium" }, render: (props) => <ResultCard {...props} /> } } }

function OverflowObserver({ cardId, onOverflow, children }) {
  const ref = useRef(null)
  useEffect(() => { const node = ref.current; if (!node) return undefined; const check = () => onOverflow(cardId, node.scrollHeight > node.clientHeight + 2 || node.scrollWidth > node.clientWidth + 2); const observer = new ResizeObserver(check); observer.observe(node); check(); return () => observer.disconnect() }, [cardId, onOverflow])
  return <div ref={ref} className="grid-card-shell">{children}</div>
}
function LayoutCanvas({ mode, viewport, snapshot, selectedId, onSelect, onLayoutCommit, onOverflow }) {
  const { width, containerRef, mounted } = useContainerWidth()
  return <div ref={containerRef} className={`layout-canvas viewport-${viewport}`}>{mounted ? <GridLayout width={width} layout={snapshot.layouts[viewport]} gridConfig={{ cols: viewport === "desktop" ? 12 : 4, rowHeight: 42, margin: [12, 12], containerPadding: [12, 12] }} dragConfig={{ enabled: mode === "layout", handle: ".result-card__handle", bounded: true }} resizeConfig={{ enabled: mode === "layout", handles: ["se"] }} onDragStop={(next) => onLayoutCommit(next, "카드 위치 변경")} onResizeStop={(next) => onLayoutCommit(next, "카드 크기 변경")}>
    {snapshot.cards.map((card) => <div key={card.id}><OverflowObserver cardId={card.id} onOverflow={onOverflow}><ResultCard {...card} selected={selectedId === card.id} onSelect={() => onSelect(card.id)} /></OverflowObserver></div>)}
  </GridLayout> : null}</div>
}
function PropertyPanel({ card, onChange, overflow }) {
  if (!card) return <aside className="property-panel"><p>카드를 선택해주세요.</p></aside>
  const onImage = (event) => { const file = event.target.files?.[0]; if (!file) return; const reader = new FileReader(); reader.onload = () => onChange({ imageUrl: reader.result, imageName: file.name }, "이미지 슬롯 변경"); reader.readAsDataURL(file) }
  return <aside className="property-panel"><span className="property-panel__badge">속성 편집</span><h2>{card.title}</h2><div className="palette-mode"><button type="button" className={card.paletteMode === "single" ? "active" : ""} onClick={() => onChange({ paletteMode: "single" }, "단색 모드 변경")}>단색</button><button type="button" className={card.paletteMode === "twoTone" ? "active" : ""} onClick={() => onChange({ paletteMode: "twoTone" }, "투톤 모드 변경")}>투톤</button></div><label>대표 색상<input type="color" value={card.accent} onChange={(event) => onChange({ accent: event.target.value }, "대표 색상 변경")} /></label>{card.paletteMode === "twoTone" ? <label>보조 색상<input type="color" value={card.secondary} onChange={(event) => onChange({ secondary: event.target.value }, "보조 색상 변경")} /></label> : null}<label>구역 배경색<input type="color" value={card.surface} onChange={(event) => onChange({ surface: event.target.value }, "배경 색상 변경")} /></label><label>글자 색상<input type="color" value={card.textColor} onChange={(event) => onChange({ textColor: event.target.value }, "글자 색상 변경")} /></label><button className="palette-auto" type="button" onClick={() => onChange(createPalette(card.accent), "대표색 자동 조합")}>대표색으로 자동 조합</button><label className="image-slot">구역 이미지<input type="file" accept="image/png,image/jpeg,image/webp" onChange={onImage} /></label>{card.imageUrl ? <button className="image-remove" type="button" onClick={() => onChange({ imageUrl: "", imageName: "" }, "이미지 제거")}>이미지 제거</button> : <p className="property-note">사람·제품 사진을 넣으면 카드 왼쪽 이미지 구역에 표시됩니다.</p>}<label>글씨 크기<strong>{LABELS[card.fontSize]}</strong><input type="range" min="0" max="4" step="1" value={LEVELS.indexOf(card.fontSize)} onChange={(event) => onChange({ fontSize: LEVELS[Number(event.target.value)] }, "글씨 크기 변경")} /></label><p className="property-note">글씨 변경은 Grid의 폭·높이를 자동 변경하지 않습니다.</p>{overflow ? <p className="property-alert">현재 크기에서 내용이 넘칩니다.</p> : <p className="property-ok">내용이 카드 안에 맞습니다.</p>}</aside>
}
function AutoPanel({ onApply }) {
  return <aside className="property-panel auto-panel"><span className="property-panel__badge">자동 정리</span><h2>화면을 보기 좋게 맞춥니다</h2><p>내용 길이·글씨 크기·대표색을 보고 PC와 모바일을 각각 정리합니다.</p><ul><li>제목은 자연스럽게 줄바꿈</li><li>내용이 긴 카드는 높이 확보</li><li>모바일은 한 줄로 정렬</li><li>대표색에서 보조색·배경·글자색 추천</li><li>투톤 색상은 이후 각각 수정 가능</li></ul><button className="auto-apply" type="button" onClick={onApply}>배치·색상 자동 정리</button><p className="property-note">Draft로만 적용되며 되돌리기로 취소할 수 있습니다.</p></aside>
}

function App() {
  const [mode, setMode] = useState("layout"), [viewport, setViewport] = useState("desktop"), [snapshot, setSnapshot] = useState(initialSnapshot), [past, setPast] = useState([]), [future, setFuture] = useState([]), [selectedId, setSelectedId] = useState(INITIAL_CARDS[0].id), [overflow, setOverflow] = useState({}), [lastChange, setLastChange] = useState("초기 Recipe")
  const commit = useCallback((next, label) => {
    if (JSON.stringify(snapshot) === JSON.stringify(next)) return
    setPast((items) => [...items, clone(snapshot)])
    setFuture([])
    setLastChange(label)
    setSnapshot(clone(next))
  }, [snapshot])
  const updateLayout = useCallback((layout, label) => commit({ ...snapshot, layouts: { ...snapshot.layouts, [viewport]: clone(layout) } }, `${viewport === "desktop" ? "PC" : "모바일"} ${label}`), [commit, snapshot, viewport])
  const updateCard = useCallback((patch, label) => commit({ ...snapshot, cards: snapshot.cards.map((card) => card.id === selectedId ? { ...card, ...patch } : card) }, label), [commit, selectedId, snapshot])
  const applyAutoLayout = useCallback(() => {
    const cards = snapshot.cards.map((card) => ({ ...card, ...createPalette(card.accent), textFit: "balanced" }))
    commit({ cards, layouts: createAutoLayouts(cards) }, "자동 배치·줄바꿈·색상 정리")
  }, [commit, snapshot.cards])
  const undo = () => { if (!past.length) return; const previous = past[past.length - 1]; setFuture((items) => [clone(snapshot), ...items]); setPast((items) => items.slice(0, -1)); setSnapshot(clone(previous)); setLastChange("되돌리기") }
  const redo = () => { if (!future.length) return; const next = future[0]; setPast((items) => [...items, clone(snapshot)]); setFuture((items) => items.slice(1)); setSnapshot(clone(next)); setLastChange("다시 실행") }
  const updateOverflow = useCallback((id, value) => setOverflow((current) => current[id] === value ? current : { ...current, [id]: value }), [])
  const puckData = useMemo(() => ({ content: snapshot.cards.map((card) => ({ type: "ResultCard", props: { ...card } })), root: { props: { title: "AI OS V2 PM3 Pilot" } } }), [snapshot.cards])
  const selectedCard = snapshot.cards.find((card) => card.id === selectedId)
  return <main className="pilot-shell"><header className="pilot-banner"><div><span className="pilot-banner__badge">PM3 격리 Pilot</span><strong>Puck + React Grid Layout</strong><small>마지막 변경: {lastChange}</small></div><div className="history-actions"><button onClick={undo} disabled={!past.length}>되돌리기</button><button onClick={redo} disabled={!future.length}>다시 실행</button><button onClick={() => commit(initialSnapshot(), "초기 Recipe 복원")}>초기 복원</button></div></header>
    <nav className="mode-toolbar" aria-label="편집 모드"><div className="segmented"><button className={mode === "structure" ? "active" : ""} onClick={() => setMode("structure")}>1. 구성요소</button><button className={mode === "layout" ? "active" : ""} onClick={() => setMode("layout")}>2. 배치·크기</button><button className={mode === "property" ? "active" : ""} onClick={() => setMode("property")}>3. 색상·글씨</button><button className={mode === "auto" ? "active" : ""} onClick={() => setMode("auto")}>4. 자동 정리</button></div><div className="segmented"><button className={viewport === "desktop" ? "active" : ""} onClick={() => setViewport("desktop")}>PC</button><button className={viewport === "mobile" ? "active" : ""} onClick={() => setViewport("mobile")}>모바일</button></div><span className="mode-help">{mode === "structure" ? "Puck이 구성요소 순서를 담당합니다." : mode === "layout" ? "카드를 끌거나 오른쪽 아래 모서리로 크기를 바꿉니다." : mode === "property" ? "Drag를 잠그고 선택한 카드만 수정합니다." : "내용을 분석해 PC·모바일 배치와 줄바꿈을 Draft로 정리합니다."}</span></nav>
    {mode === "structure" ? <section className="puck-stage"><Puck config={puckConfig} data={puckData} headerTitle="구성요소 편집" headerPath="V2 / PM3 / 구조 모드" onPublish={() => setLastChange("Puck 구조 검증 저장")} /></section> : <section className={`workspace-stage mode-${mode}`}><LayoutCanvas mode={mode} viewport={viewport} snapshot={snapshot} selectedId={selectedId} onSelect={setSelectedId} onLayoutCommit={updateLayout} onOverflow={updateOverflow} />{mode === "property" ? <PropertyPanel card={selectedCard} onChange={updateCard} overflow={overflow[selectedId]} /> : null}{mode === "auto" ? <AutoPanel onApply={applyAutoLayout} /> : null}</section>}
    <footer className="pilot-footer"><span>카드 3개</span><span>PC·모바일 Recipe 분리</span><span>Drag 소유권: {mode === "structure" ? "Puck" : mode === "layout" ? "RGL" : "잠금"}</span><span>기록 {past.length}개</span></footer></main>
}
ReactDOM.createRoot(document.getElementById("root")).render(<React.StrictMode><App /></React.StrictMode>)
