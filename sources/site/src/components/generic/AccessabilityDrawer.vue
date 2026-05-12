<template>
  <wa-button class="accessability-btn" variant="white" outline @click="state.drawerOpen = !state.drawerOpen"
    title="Optionen für Barrierefreiheit">
    <wa-icon name="universal-access"></wa-icon>
  </wa-button>

  <wa-drawer label="Optionen für Barrierefreiheit" class="drawer-overview" @wa-hide="state.drawerOpen = false"
    :open="state.drawerOpen ? true : null">
    <wa-button @click="state.drawerOpen = false" class="drawer-close-btn" slot="header-actions">
      <wa-icon name="chevron-right"></wa-icon>
    </wa-button>

    <div class="access-option-wrap">
      <wa-button class="access-option-btn"
        :class="accessabilityStore.state.cursorSize != 'default' ? 'is-selected' : ''" outline variant="white" size=""
        @click="setCursorSize()">
        <wa-icon name="check" class="access-active-icon"></wa-icon>
        <wa-icon name="arrow-pointer" class="access-option-icon"></wa-icon>
        <div class="access-option-name">Großer Zeiger</div>
      </wa-button>

      <wa-button class="access-option-btn"
        :class="accessabilityStore.state.contrastMode != 'default' ? 'is-selected' : ''" outline variant="white" size=""
        @click="setContrastMode()">
        <wa-icon name="check" class="access-active-icon"></wa-icon>
        <wa-icon name="circle-half-stroke" class="access-option-icon"></wa-icon>
        <div class="access-option-name">
          {{
            accessabilityStore.state.contrastMode === 'invert'
              ? 'Invertierter Kontrast'
              : accessabilityStore.state.contrastMode === 'dark'
                ? 'Dunkler Kontrast'
                : accessabilityStore.state.contrastMode === 'light'
                  ? 'Heller Kontrast'
                  : 'Kontrast'
          }}
        </div>
      </wa-button>

      <wa-button class="access-option-btn" :class="accessabilityStore.state.fontSize != 0 ? 'is-selected' : ''" outline
        variant="white" size="" @click="setFontSize()">
        <wa-icon name="check" class="access-active-icon"></wa-icon>
        <wa-icon name="text-width" class="access-option-icon"></wa-icon>
        <div class="access-option-name">Textgröße</div>
        <div class="access-option-amount access-option-amount-3">
          <div class="access-amount-bar" v-for="i in accessabilityStore.state.fontSize" :key="i"></div>
        </div>
      </wa-button>

      <wa-button class="access-option-btn" :class="accessabilityStore.state.lineHeight != 0 ? 'is-selected' : ''"
        outline variant="white" size="" @click="setLineHeight()">
        <wa-icon name="check" class="access-active-icon"></wa-icon>
        <wa-icon name="text-height" class="access-option-icon"></wa-icon>
        <div class="access-option-name">Zeilenhöhe</div>
        <div class="access-option-amount access-option-amount-3">
          <div class="access-amount-bar" v-for="i in accessabilityStore.state.lineHeight" :key="i"></div>
        </div>
      </wa-button>

      <wa-button class="access-option-btn"
        :class="accessabilityStore.state.fontFamily != 'default' ? 'is-selected' : ''" outline variant="white" size=""
        @click="setFontFamily()">
        <wa-icon name="check" class="access-active-icon"></wa-icon>
        <wa-icon name="font" class="access-option-icon"></wa-icon>
        <div class="access-option-name">
          {{
            accessabilityStore.state.fontFamily === 'dyslexic'
              ? 'Legasthenie freundlich'
              : accessabilityStore.state.fontFamily === 'inclusive'
                ? 'Einfach Lesbar'
                : 'Schriftart'
          }}
        </div>
      </wa-button>

      <!--<wa-button class="access-option-btn"
          :class="accessabilityStore.state.currentLanguage != 'de' ? 'is-selected' : ''"
          outline
          variant="white"
          size=""
          @click="setLanguage()">
            <wa-icon name="check-lg" class="access-active-icon"></wa-icon>
            <wa-icon name="translate" class="access-option-icon"></wa-icon>
            <div class="access-option-name">Einfache Sprache</div>
        </wa-button>-->

      <wa-button class="access-option-btn" :class="accessabilityStore.state.textAlign != 'default' ? 'is-selected' : ''"
        outline variant="white" size="" @click="setTextAlign()">
        <wa-icon name="check" class="access-active-icon"></wa-icon>
        <wa-icon :name="{
          left: 'align-left',
          center: 'align-center',
          right: 'align-right'
        }[accessabilityStore.state.textAlign] || 'align-left'" class="access-option-icon"></wa-icon>
        <div class="access-option-name">
          {{
            {
              left: 'Text linksbündig',
              center: 'Text zentriert',
              right: 'Text rechtsbündig'
            }[accessabilityStore.state.textAlign] || 'Text ausrichten'
          }}
        </div>
      </wa-button>

      <wa-button class="access-option-btn" :class="accessabilityStore.state.linksHighlighted ? 'is-selected' : ''"
        outline variant="white" size="" @click="setLinksHighlighted()">
        <wa-icon name="check" class="access-active-icon"></wa-icon>
        <wa-icon name="link" class="access-option-icon"></wa-icon>
        <div class="access-option-name">Links hervorbehen</div>
      </wa-button>

      <wa-button class="access-option-btn" :class="accessabilityStore.state.infoHints ? 'is-selected' : ''" outline
        variant="white" size="" @click="setInfoHints()">
        <wa-icon name="check" class="access-active-icon"></wa-icon>
        <wa-icon name="circle-info" class="access-option-icon"></wa-icon>
        <div class="access-option-name">Kurzinfos</div>
      </wa-button>

      <wa-button class="access-option-btn" :class="accessabilityStore.state.hideImages ? 'is-selected' : ''" outline
        variant="white" size="" @click="setHideImages()">
        <wa-icon name="check" class="access-active-icon"></wa-icon>
        <wa-icon name="image" class="access-option-icon"></wa-icon>
        <div class="access-option-name">Bilder ausblenden</div>
      </wa-button>

      <wa-button class="access-option-btn" outline variant="white" size="" @click="showPageStructure()">
        <wa-icon name="list" class="access-option-icon"></wa-icon>
        <div class="access-option-name">Seitenstruktur anzeigen</div>
      </wa-button>

      <wa-dialog label="Seitenstrucktur" :open="state.showPageStructure ? true : null"
        @wa-hide="state.showPageStructure = false">
        <wa-tab-group>
          <wa-tab slot="nav" panel="headlines">Überschriften</wa-tab>
          <wa-tab slot="nav" panel="sections">Abschnitte</wa-tab>
          <wa-tab slot="nav" panel="links">Links</wa-tab>

          <wa-tab-panel name="headlines">
            <a @click="scrollToEl(element)" class="structure-item" :class="'structure-item-' + element.nodeName"
              v-for="element in state.structureHeadlines">
              <div class="structure-item-type">{{ element.nodeName }}</div>
              <div class="structure-item-content">{{ element.innerText }}</div>
            </a>
          </wa-tab-panel>
          <wa-tab-panel name="sections">
            <a @click="scrollToEl(element)" class="structure-item" :class="'structure-item-' + element.nodeName"
              v-for="element in state.structureSections">
              <div class="structure-item-type">
                <wa-icon name="code"></wa-icon>
              </div>
              <div class="structure-item-content">
                {{
                  element.title
                    ? element.title
                    : element.ariaLabel
                      ? element.ariaLabel
                      : element.nodeName
                }}
              </div>
            </a>
          </wa-tab-panel>
          <wa-tab-panel name="links">
            <a :href="element.href" class="structure-item" v-for="element in state.structureLinks">
              <div class="structure-item-type">
                <wa-icon name="link"></wa-icon>
              </div>
              <div class="structure-item-content">{{ element.innerText ? element.innerText : element.title }}</div>
            </a>
          </wa-tab-panel>
        </wa-tab-group>
      </wa-dialog>

      <wa-button outline variant="white" pill class="clear-all-btn" @click="clearAll()">
        Alle Optionen auschalten
      </wa-button>
      <wa-button outline variant="primary" pill class="clear-all-btn" href="mailto:mail@mausbrand.de">
        Barriere melden
      </wa-button>


    </div>
  </wa-drawer>
</template>

<script setup>
import { onMounted, reactive, ref, watch } from "vue";
import { useAccessabilityStore } from "@/stores/accessabilityStore";
import { Request } from "@viur/vue-utils";

const accessabilityStore = useAccessabilityStore();
const appElement = document.getElementById("vite_context");

const state = reactive({
  drawerOpen: false,
  cursorSize: "default",
  contrastAmount: "",
  textSize: "",
  lineHeight: "",
  linksHighlight: "",
  showPageStructure: false,
  structureHeadlines: [],
  structureLinks: []
});

function setCursorSize() {
  accessabilityStore.state.cursorSize =
    accessabilityStore.state.cursorSize === "default" ? "big" : "default";

  ["default", "big"].forEach(family => {
    appElement.classList.remove(`app-cursor-size-${family}`);
  });

  appElement.classList.add(`app-cursor-size-${accessabilityStore.state.cursorSize}`);
}

function setFontSize() {
  accessabilityStore.state.fontSize =
    (accessabilityStore.state.fontSize + 1) % 4;

  [0, 1, 2, 3].forEach(i => {
    appElement.classList.remove(`app-font-size-${i}`);
  });

  appElement.classList.add(`app-font-size-${accessabilityStore.state.fontSize}`);
}

function setLineHeight() {
  accessabilityStore.state.lineHeight =
    (accessabilityStore.state.lineHeight + 1) % 4;

  [0, 1, 2, 3].forEach(i => {
    appElement.classList.remove(`app-line-height-${i}`);
  });

  appElement.classList.add(`app-line-height-${accessabilityStore.state.lineHeight}`);
}

function setLinksHighlighted() {
  accessabilityStore.state.linksHighlighted = !accessabilityStore.state.linksHighlighted;

  ["true", "false"].forEach(mode => {
    appElement.classList.remove(`app-links-highlighted-${mode}`);
  });
  appElement.classList.add('app-links-highlighted-' + accessabilityStore.state.linksHighlighted)
}

function setFontFamily() {
  const fonts = ["default", "dyslexic", "inclusive"];
  const currentFont = accessabilityStore.state.fontFamily;
  const nextIndex = (fonts.indexOf(currentFont) + 1) % fonts.length;
  const nextFont = fonts[nextIndex];

  accessabilityStore.state.fontFamily = nextFont;

  ["default", "dyslexic", "inclusive"].forEach(family => {
    appElement.classList.remove(`app-font-family-${family}`);
  });

  appElement.classList.add(`app-font-family-${accessabilityStore.state.fontFamily}`);
}

function setContrastMode() {
  const modes = ["default", "invert", "dark", "light"];
  const currentMode = accessabilityStore.state.contrastMode;
  const nextIndex = (modes.indexOf(currentMode) + 1) % modes.length;
  const nextMode = modes[nextIndex];

  accessabilityStore.state.contrastMode = nextMode;

  // Alte Klassen entfernen (optional, aber sicherheitshalber)
  modes.forEach(mode => {
    appElement.classList.remove(`app-contrast-mode-${mode}`);
  });

  // Neue Klasse hinzufügen
  appElement.classList.add(`app-contrast-mode-${nextMode}`);
}

function setHideImages() {
  accessabilityStore.state.hideImages = !accessabilityStore.state.hideImages;

  ["true", "false"].forEach(family => {
    appElement.classList.remove(`app-hide-images-${family}`);
  });
  appElement.classList.add('app-hide-images-' + accessabilityStore.state.hideImages)

}

function setTextAlign() {
  const modes = ["default", "left", "center", "right"];
  const currentMode = accessabilityStore.state.textAlign;
  const nextIndex = (modes.indexOf(currentMode) + 1) % modes.length;
  const nextMode = modes[nextIndex];

  accessabilityStore.state.textAlign = nextMode;

  // Alte Klassen entfernen (optional, aber sicherheitshalber)
  modes.forEach(mode => {
    appElement.classList.remove(`app-text-align-${mode}`);
  });

  // Neue Klasse hinzufügen
  appElement.classList.add(`app-text-align-${nextMode}`);
}

async function setLanguage() {
  accessabilityStore.state.currentLanguage =
    accessabilityStore.state.currentLanguage === "de" ? "de-x-simple" : "de";

  let data = await Request.get("/set_lang/" + accessabilityStore.state.currentLanguage).then(async (resp) => {
    return resp.status === 200;
  });
  if (data) {
    location.reload();
  }
}

function setInfoHints() {
  accessabilityStore.state.infoHints = !accessabilityStore.state.infoHints;
  hideInfoHints();
}

let hintElements = [];

function showInfoHints() {
  if (!accessabilityStore.state.infoHints) {
    // Tooltip-Events entfernen
    hintElements.forEach(el => {
      el.removeEventListener('mouseenter', el._showHint);
      el.removeEventListener('mousemove', el._moveHint);
      el.removeEventListener('mouseleave', el._hideHint);
      delete el._showHint;
      delete el._moveHint;
      delete el._hideHint;
    });
    hintElements = [];
    return;
  }

  hintElements = [
    ...new Set([
      ...document.querySelectorAll('[href]'),
      ...document.querySelectorAll('wa-button')
    ])
  ];

  hintElements.forEach(el => {
    let tooltip;

    const showHint = (e) => {
      const text = el.getAttribute('title') || el.textContent.trim();
      if (!text) return;

      tooltip = document.createElement('div');
      tooltip.className = 'dynamic-tooltip';
      tooltip.textContent = text;
      document.body.appendChild(tooltip);
      positionTooltip(e);
    };

    const moveHint = (e) => {
      if (tooltip) positionTooltip(e);
    };

    const hideHint = () => {
      if (tooltip) {
        tooltip.remove();
        tooltip = null;
      }
    };

    const positionTooltip = (e) => {
      const offset = 20;
      const tooltipWidth = tooltip.offsetWidth || 150; // Fallback falls noch nicht gerendert
      const isRightSide = e.pageX > window.innerWidth / 2;

      // Positionierung abhängig von der Fensterhälfte
      if (isRightSide) {
        tooltip.style.left = (e.pageX - tooltipWidth - offset) + 'px';
      } else {
        tooltip.style.left = (e.pageX + offset) + 'px';
      }

      tooltip.style.top = (e.pageY + offset) + 'px';
    };

    el._showHint = showHint;
    el._moveHint = moveHint;
    el._hideHint = hideHint;

    el.addEventListener('mouseenter', showHint);
    el.addEventListener('mousemove', moveHint);
    el.addEventListener('mouseleave', hideHint);
  });
}

watch(() => accessabilityStore.state.infoHints, () => {
  showInfoHints();
});

function hideInfoHints() {
  let tooltips = document.querySelectorAll('.dynamic-tooltip');

  tooltips.forEach(el => {
    el.remove();
  });
}

function showPageStructure() {
  state.showPageStructure = !state.showPageStructure;
}

function getPageStructure() {
  const headlines = document.querySelectorAll("h1, h2, h3, h4, h5, h6")

  state.structureHeadlines = Array.from(headlines);

  const links = document.querySelectorAll("a")
  state.structureLinks = Array.from(links);

  const sections = document.querySelectorAll("header, main, nav, section, footer, form")
  state.structureSections = Array.from(sections);
}

function scrollToEl(element) {
  element.scrollIntoView();
  state.showPageStructure = false;
}

async function clearAll() {
  accessabilityStore.state.cursorSize = "default";
  accessabilityStore.state.cursorSize = "default";
  accessabilityStore.state.fontSize = 0;
  accessabilityStore.state.lineHeight = 0,
    accessabilityStore.state.linksHighlighted = false;
  accessabilityStore.state.fontFamily = "default";
  accessabilityStore.state.contrastMode = "default";
  accessabilityStore.state.hideImages = false;
  accessabilityStore.state.textAlign = "default";
  accessabilityStore.state.currentLanguage = "de";
  accessabilityStore.state.infoHints = false;

  let data = await Request.get("/set_lang/" + accessabilityStore.state.currentLanguage).then(async (resp) => {
    return resp.status === 200;
  });
  if (data) {
    location.reload();
  }
}

onMounted(() => {
  getPageStructure()
  showInfoHints()
})
</script>

<style scoped>
.accessability-btn {
  position: fixed;
  right: var(--wa-space-l);
  bottom: var(--wa-space-l);
  border-radius: 50%;
  box-shadow: 0 0 10px 0 rgba(0, 0, 0, .25);
  z-index: 29;

  &::part(base) {
    padding: 0;
    aspect-ratio: 1;
    border-radius: 50%;
  }

  &::part(label) {
    display: flex;
    justify-content: center;
    align-self: center;
    padding: var(--wa-space-s);
    aspect-ratio: 1;
    font-size: 2.5em;
  }

  wa-icon {
    background-color: transparent !important;
    color: #000 !important;
    transition: all ease .3s;
  }

  &:hover wa-icon {
    color: #fff !important;
  }
}

.drawer-overview {
  &::part(base) {
    z-index: 30;
  }

  &::part(overlay) {
    display: none;
  }

  &::part(header-actions) {
    padding-right: 0;
  }

  &::part(header) {
    background: var(--ignt-color-gradient);
    color: #fff;
  }

  &::part(close-button) {
    display: none;
  }
}

.drawer-close-btn {
  aspect-ratio: 1;
  height: 100%;
  background-color: transparent !important;
  color: #fff !important;
  transform: all ease .3s;

  &::part(base) {
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 1.5em;
    width: 100%;
    height: 100%;
  }

  &:hover {
    font-size: 1.1em;

    &::part(base) {
      color: #fff;
    }
  }
}

.access-option-wrap {
  width: 100%;
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: var(--wa-space-l)
}

.access-option-btn {
  &::part(base) {
    display: flex;
    box-shadow: none !important;
    background-color: transparent !important;
    width: 100%;
    aspect-ratio: 4 / 3;
    border-radius: var(--ignt-border-radius-default);
  }


  &::part(label) {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: var(--wa-space-m);
    width: 100%;
    white-space: initial;
  }

  &:hover {
    &::part(base) {
      box-shadow: none !important;
      background-color: transparent !important;
      color: var(--wa-color-text-default) !important;
    }
  }

  &.is-selected {
    &::part(base) {
      border: 2px solid var(--ignt-color-primary);
    }

    .access-active-icon {
      display: flex;
    }
  }
}

.access-option-name {
  font-size: 1.2em;
  font-weight: 600;
}

.access-active-icon {
  display: none;
  ;
  background-color: var(--ignt-color-primary);
  border-radius: 50%;
  color: #fff;
  font-size: 1em;
  padding: var(--wa-space-2xs);
  position: absolute;
  top: var(--wa-space-m);
  right: var(--wa-space-m);
}

.access-option-icon {
  font-size: 2em;
  margin-bottom: var(--wa-space-s);
}


.access-option-amount {
  display: grid;
  gap: var(--wa-space-s);
  position: absolute;
  left: var(--wa-space-s);
  bottom: var(--wa-space-s);
  right: var(--wa-space-s);
  background-color: transparent !important;

  &.access-option-amount-3 {
    grid-template-columns: repeat(3, minmax(0, 1fr))
  }
}

.access-amount-bar {
  height: 4px;
  border-radius: 2px;
  background-color: var(--ignt-color-primary);
}

.structure-item {
  --margin: var(--wa-space-l);

  display: flex;
  flex-direction: row;
  flex-wrap: nowrap;
  align-items: center;
  gap: var(--wa-space-m);
  margin-bottom: var(--wa-space-l);
  cursor: pointer;

  &.structure-item-H2 {
    margin-left: var(--margin);
  }

  &.structure-item-H3 {
    margin-left: calc(2 * var(--margin));
  }

  &.structure-item-H4 {
    margin-left: calc(3 * var(--margin));
  }

  &.structure-item-H5 {
    margin-left: calc(4 * var(--margin));
  }

  &.structure-item-H6 {
    margin-left: calc(5 * var(--margin));
  }
}

.structure-item-type {
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: var(--ignt-color-primary);
  color: #fff;
  padding: var(--wa-space-xs) var(--wa-space-s);
  border-radius: var(--ignt-border-radius-default);
  cursor: pointer;
}

.clear-all-btn {
  grid-column: span 2;
}

.app-contrast-mode-dark {
  * {
    background-color: var(--wa-color-neutral-1000) !important;
    color: var(--wa-color-neutral-0) !important;
    background: var(--wa-color-neutral-1000) !important;
  }

  wa-dialog::part(panel) {
    background-color: var(--wa-color-neutral-1000) !important;
    color: var(--wa-color-neutral-0) !important;
    background: var(--wa-color-neutral-1000) !important;
  }

  wa-tab::part(base) {
    color: var(--wa-color-neutral-0) !important;
  }

  .drawer-overview {

    &::part(header),
    &::part(body),
    &::part(footer) {
      background-color: var(--wa-color-neutral-1000) !important;
      color: var(--wa-color-neutral-0) !important;
    }
  }

  .access-option-btn::part(base) {
    border-color: var(--wa-color-neutral-0) !important;
  }

  .access-active-icon {
    border: 1px solid var(--wa-color-neutral-0);
  }

  .access-amount-bar {
    background-color: var(--wa-color-neutral-0) !important;
  }

  .structure-item-type {
    border: 1px solid var(--wa-color-neutral-0);
  }

  .structure-item-content {
    color: #ff0 !important
  }
}

.app-contrast-mode-light {

  .access-amount-bar {
    background-color: var(--wa-color-neutral-1000) !important;
  }

  .access-active-icon {
    border: 1px solid var(--wa-color-neutral-1000);
  }

  .structure-item-type {
    border: 1px solid var(--wa-color-neutral-1000);
  }

  .structure-item-content {
    color: #00f !important;
  }
}
</style>
